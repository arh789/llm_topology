#!/usr/bin/env node
"use strict";
// R020 higher-order semantic continuity screen. Non-destructive and deterministic.
// Node CLI usage: node R020_SEMANTIC_CONTINUITY_REPRODUCER.js [run_directory]
// Requires the original measured chatgpt_community_networks.json and prompt_records.json.
// Writes derived JSON only to STDOUT; redirect it into a new versioned analysis file.
const fs=require("node:fs"),path=require("node:path");
function analyse(raw,prompt){
 // BEGIN-PURE-R020-ANALYSIS

  // This is an evidence-anchored semantic *screen*: labels are provisional,
  // never substituted for the original community and measured token edge IDs.
  const GROUPS = {
    settlement:"city cities town towns village villages settlement settlements municipality municipal urban suburb suburbs county counties communities community neighbourhood neighborhood districts district metropolitan township",
    built_places:"building buildings house houses housing courtyard courtyards shop shops hotel hotels street streets structures structure corridor corridors archway architecture architectural apartment apartments",
    water_terrain:"river rivers lake lakes water waters drainage flood floods groundwater ocean oceans sea seas wetland wetlands canal canals coast coastline shore shores coastal valley valleys creek creeks waterway waterways stream streams",
    movement_routes:"road roads roadway roadways highways highway railway railways train trains path paths routes route travel travelling traveling travel transportation transport transporting transported traffic journey journeys trips trip walking walked movement movements moving navigate transit vehicle vehicles airport airports pedestrian pedestrians truck trucks mobility voyage voyages",
    connection_crossing:"bridge bridges bridging cross crossing crossings connection connections connect connecting connects junction junctions linking links link passage passages access barrier barriers span spans tunnel tunnels transfer transfers ferry ferries traversing traverse",
    inhabitants:"residents resident citizens citizen people persons population populations inhabitants inhabitant settlers settler families family workers worker",
    hazards:"flood floods flooding storms storm catastrophe catastrophes disaster disasters destruction destroyed damage damaged interruption interrupt blocked obstacle obstruction obstructions collision collisions fires fire explosions explosion rebellion collapsed collapse",
    repair_reconstruction:"rebuilding rebuild reconstruction reconstruct renovation renovations restoration restore restored repairing repaired repair repairs stabilisation stabilization rescue recovery",
    engineering_governance:"engineer engineers engineering construction construct constructing constructed concrete steel beams beam foundation foundations infrastructure government governance council councils planning planner planners design designs designing designed architect architects materials material",
    commerce:"trade commerce goods markets market commercial economic economy business businesses supply logistics freight shipping delivery deliveries merchants",
    evaluation:"intriguing fascinating unfortunate noteworthy prominent mysterious wonderful magnificent comparable similar remarkable incredible",
    scholarship:"scholar scholars academics academic professor professors knowledge science research researcher researchers expertise theology theological ologist",
    operations:"regulates regulate inhibit inhibits activate activates transforms transformation transformations measurement measurements control controls managing management",
    biology:"cells cell fibroblast lymphocyte macrophages genes genetics disease medical therapy treatments diagnosis lungs kidney"
  };
  const ROLE_ORDER = Object.keys(GROUPS);
  const TASK_ROLES = ROLE_ORDER.slice(0,10);
  const BACKGROUND_ROLES = ROLE_ORDER.slice(10);
  const WORDS=Object.fromEntries(Object.entries(GROUPS).map(([k,v])=>[k,new Set(v.split(" "))]));
  const norm=x=>String(x).replace(/^␠/,"").trim().toLowerCase();
  const title=x=>String(x).replace(/^␠/,"").trim();
  const r3=x=>Math.round(x*1000)/1000;
  const seenKeys=new Set();
  const annotatedGraphs=[];
  let classifiedCount=0;
  let edgeCount=0;
  function classify(c){
    const hits=[];
    for(const [role,termset] of Object.entries(WORDS)){
      const r=[...new Set(c.representative_tokens.map(norm).filter(t=>termset.has(t)))];
      const e=[...new Set(c.most_extreme_tokens.map(norm).filter(t=>termset.has(t)&&!r.includes(t)))];
      // Two independent exemplar words are needed; one rep + two extra
      // extreme tokens may qualify, but confidence remains lower.
      if(r.length>=2 || (r.length>=1 && e.length>=2)){
        hits.push({role,weight:r3(r.length+0.3*e.length),representatives:r.slice(0,8),extremes:e.slice(0,5),evidence_kind:r.length>=2?"multiple_representatives":"rep_plus_extremes"});
      }
    }
    hits.sort((a,b)=>b.weight-a.weight||a.role.localeCompare(b.role));
    return hits.slice(0,3);
  }
  for(const g of raw.networks){
    const key=g.decision_index+"|"+g.state_index+"|"+g.side;
    if(seenKeys.has(key))throw Error("Repeated measured network "+key);
    seenKeys.add(key);
    const communities=g.communities.map(c=>({id:c.community_id,size:c.community_size,exemplars:c.representative_tokens.slice(0,6).map(title),hits:classify(c)}));
    classifiedCount+=communities.filter(c=>c.hits.length>0).length;
    const cm=new Map(communities.map(c=>[c.id,c]));
    let familyEdges=[], selectedEdges=0;
    for(const e of g.intercommunity_edges){
      edgeCount++;
      const ca=cm.get(e.community_a),cb=cm.get(e.community_b);
      if(!ca||!cb)throw Error("Orphan community edge at "+key);
      const affinity=e.token_edge_count/Math.sqrt(ca.size*cb.size);
      if(affinity<0.30||e.token_edge_count<30)continue;
      selectedEdges++;
      for(const aa of ca.hits)for(const bb of cb.hits){
        if(aa.role===bb.role)continue;
        const ordered=[aa.role,bb.role].sort();
        const pair=ordered.join(" ↔ ");
        const isTask=TASK_ROLES.includes(aa.role)&&TASK_ROLES.includes(bb.role);
        const category=isTask?"question_related_candidate":"background_or_cross_domain";
        familyEdges.push({pair,category,a:ca.id,b:cb.id,
          role_a:aa.role,role_b:bb.role,
          token_edges:e.token_edge_count,affinity:r3(affinity),
          a_tokens:aa.representatives.slice(0,5),b_tokens:bb.representatives.slice(0,5),
          a_exemplars:ca.exemplars,b_exemplars:cb.exemplars});
      }
    }
    const pairMap=new Map();
    for(const e of familyEdges){
      const k=e.pair+"|"+e.category;
      if(!pairMap.has(k))pairMap.set(k,{pair:e.pair,category:e.category,measured_links:0,token_edges:0,strongest_affinity:0,evidence:[]});
      const o=pairMap.get(k);
      o.measured_links++;o.token_edges+=e.token_edges;o.strongest_affinity=Math.max(o.strongest_affinity,e.affinity);
      if(o.evidence.length<5)o.evidence.push(e);
    }
    const pairs=[...pairMap.values()].sort((a,b)=>b.token_edges-a.token_edges||a.pair.localeCompare(b.pair));
    const roleEvidence=[];
    for(const role of ROLE_ORDER){
      const matching=communities.filter(c=>c.hits.some(x=>x.role===role));
      if(matching.length)roleEvidence.push({role,communities:matching.map(c=>({
        id:c.id,size:c.size,exemplars:c.exemplars,anchor_matches:c.hits.find(x=>x.role===role).representatives
      }))});
    }
    annotatedGraphs.push({decision:g.decision_index+1,state:g.state_index,sector:g.side,
      community_count:communities.length,selected_relation_edges:selectedEdges,
      retained_semantic_links:familyEdges.length,
      roles:roleEvidence,pairs,
      unresolved_large_communities:communities.filter(c=>c.hits.length===0)
        .sort((a,b)=>b.size-a.size).slice(0,4).map(c=>({id:c.id,size:c.size,exemplars:c.exemplars}))});
  }
  if(seenKeys.size!==512||raw.network_count!==512)throw Error("Not 512 networks");
  const tokens=prompt.generated_decoded_tokens||[];
  if(tokens.length!==32)throw Error("Not 32 generated tokens");
  const decisions=[];
  const phases=[{name:"input",states:[0]},{name:"contextual",states:[1,2,3,4,5]},{name:"output_proximal",states:[6,7]}];
  for(let d=1;d<=32;d++){
    const networks=annotatedGraphs.filter(g=>g.decision===d);
    if(networks.length!==16)throw Error("Missing network in decision "+d);
    const curr=d===1?":":tokens[d-2];
    const next=tokens[d-1];
    const map=new Map();
    for(const graph of networks){
      for(const pair of graph.pairs){
        let k=pair.category+"|"+pair.pair;
        if(!map.has(k))map.set(k,{pair:pair.pair,category:pair.category,states:new Set(),phase:new Set(),sectors:new Set(),snapshots:0,measured_links:0,token_edges:0,evidence:[]});
        const item=map.get(k);item.states.add(graph.state);
        item.phase.add(graph.state===0?"input":graph.state<=5?"contextual":"output_proximal");
        item.sectors.add(graph.sector);item.snapshots++;item.measured_links+=pair.measured_links;item.token_edges+=pair.token_edges;
        if(item.evidence.length<6){
          const ed=pair.evidence[0];item.evidence.push({state:graph.state,sector:graph.sector,
            communities:[ed.a,ed.b],role_a:ed.role_a,role_b:ed.role_b,
            token_edges:ed.token_edges,affinity:ed.affinity,
            tokens_a:ed.a_tokens,tokens_b:ed.b_tokens});
        }
      }
    }
    const relations=[...map.values()].map(x=>({...x,
      states:[...x.states].sort((a,b)=>a-b),phases:[...x.phase].sort(),sectors:[...x.sectors].sort(),
      status:[...x.states].filter(s=>s>=1&&s<=5).length>=2?"recurrent_contextual_candidate":
        [...x.states].some(s=>s>=1&&s<=5)?"single_contextual_state_candidate":
        [...x.states].includes(0)?"input_neighbourhood_only":"output_proximal_only"}))
      .sort((a,b)=>b.states.filter(s=>s>=1&&s<=5).length-a.states.filter(s=>s>=1&&s<=5).length||b.token_edges-a.token_edges||a.pair.localeCompare(b.pair));
    const taskRelations=relations.filter(x=>x.category==="question_related_candidate"&&x.sectors.includes("positive_head"));
    const negativeTaskRelations=relations.filter(x=>x.category==="question_related_candidate"&&x.sectors.includes("negative_tail"));
    const topPerState=networks.map(g=>({state:g.state,sector:g.sector,
      anchor_roles:g.roles.map(x=>x.role),
      strongest_task_links:g.pairs.filter(p=>p.category==="question_related_candidate").slice(0,6).map(p=>({
        pair:p.pair,token_edges:p.token_edges,exemplar:p.evidence[0]&&{communities:[p.evidence[0].a,p.evidence[0].b],tokens_a:p.evidence[0].a_tokens,tokens_b:p.evidence[0].b_tokens,affinity:p.evidence[0].affinity}
      })),
      strongest_other_links:g.pairs.filter(p=>p.category!=="question_related_candidate").slice(0,3).map(p=>({pair:p.pair,token_edges:p.token_edges})),
      unresolved_examples:g.unresolved_large_communities.slice(0,2)}));
    decisions.push({decision:d,current_input:curr,next_token:next,
      semantic_relations:taskRelations,
      negative_sector_relation_candidates:negativeTaskRelations,
      background_relations:relations.filter(x=>x.category!=="question_related_candidate").slice(0,10),
      phase_summary:phases.map(ph=>({phase:ph.name,
        distinct_task_relations:taskRelations.filter(t=>t.states.some(s=>ph.states.includes(s))).length,
        relation_names:taskRelations.filter(t=>t.states.some(s=>ph.states.includes(s))).map(t=>t.pair),
        positive_anchor_families:[...new Set(networks.filter(g=>ph.states.includes(g.state)&&g.sector==="positive_head").flatMap(g=>g.roles.filter(r=>TASK_ROLES.includes(r.role)).map(r=>r.role)))].sort()})),
      detail:topPerState});
  }
  const pairsByName=new Map();
  for(const row of decisions){
    for(const p of row.semantic_relations){
      if(!pairsByName.has(p.pair))pairsByName.set(p.pair,{pair:p.pair,decisions:[],input_decisions:[],contextual_decisions:[],output_decisions:[],input_types:new Set(),contextual_input_types:new Set(),states:new Set(),evidence:[]});
      const out=pairsByName.get(p.pair);out.decisions.push(row.decision);out.input_types.add(norm(row.current_input));
      if(p.phases.includes("input"))out.input_decisions.push(row.decision);
      if(p.phases.includes("contextual")){out.contextual_decisions.push(row.decision);out.contextual_input_types.add(norm(row.current_input))}
      if(p.phases.includes("output_proximal"))out.output_decisions.push(row.decision);
      for(const s of p.states)out.states.add(s);
      if(out.evidence.length<14&&p.evidence.length)out.evidence.push({decision:row.decision,...p.evidence[0]});
    }
  }
  const globalPairs=[...pairsByName.values()].map(x=>({...x,
    input_types:[...x.input_types],contextual_input_types:[...x.contextual_input_types],
    states:[...x.states].sort((a,b)=>a-b),
    decision_count:x.decisions.length,contextual_decision_count:x.contextual_decisions.length}))
    .sort((a,b)=>b.contextual_decision_count-a.contextual_decision_count||b.decision_count-a.decision_count||a.pair.localeCompare(b.pair));
  const matchedByStage=Array.from({length:8},(_,state)=>({
    state,
    mean_distinct_task_relations_per_decision:r3(decisions.reduce((sum,row)=>sum+row.semantic_relations.filter(p=>p.states.includes(state)).length,0)/32),
    decisions_with_any_task_relation:decisions.filter(row=>row.semantic_relations.some(p=>p.states.includes(state))).length,
    decisions_with_positive_anchor:decisions.filter(row=>row.detail.some(g=>g.state===state&&g.sector==="positive_head"&&g.anchor_roles.some(f=>TASK_ROLES.includes(f)))).length
  }));
  const output={
    schema_version:1,
    run_id:raw.run_id,
    analytical_boundary:"candidate functional families inferred through curated exemplar anchors AND measured direct intercommunity edges; these are prompts to semantic reasoning, not automatic semantic identities",
    source_network_count:raw.network_count,community_count:raw.networks.reduce((s,g)=>s+g.communities.length,0),
    measured_intercommunity_edges_examined:edgeCount,communities_with_some_anchor:classifiedCount,
    min_direct_edge_count:30,min_normalised_edge_affinity:0.30,
    phases,seed_roles:GROUPS,decision_maps:decisions,
    cross_decision_relations:globalPairs,state_summary:matchedByStage,
    limits:["Selection of semantic anchor words is interpretive, not an independently blinded discovery.",
      "Measured links indicate vocabulary-neighbour connections, not causal or logical propositions.",
      "An unlabelled community remains in the source network. No inferred absence from failure to match words.",
      "Identical word stems or morphology are not independent evidence of stable semantic parents.",
      "A relation persisting across states means related exemplar families recur in measured linked communities; it does not show continuity of one underlying hidden mechanism.",
      "S06-S07 input-embedding projections may contain pervasive shared geometric backgrounds; the output-head matrix is untied.",
      "One prompt and a self-repeated response cannot separate all prompt conditioning from token identity."]
  };
  return output;

 // END-PURE-R020-ANALYSIS
}
if(require.main===module){
 const root=process.argv[2] ? path.resolve(process.argv[2]) : path.resolve(__dirname,"..");
 const raw=JSON.parse(fs.readFileSync(path.join(root,"chatgpt_community_networks.json"),"utf8"));
 const prompt=JSON.parse(fs.readFileSync(path.join(root,"prompt_records.json"),"utf8"));
 process.stdout.write(JSON.stringify(analyse(raw,prompt),null,2)+"\n");
}
module.exports={analyse};
