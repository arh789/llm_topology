// Reproduce the R020 provisional semantic candidate inventory locally with Node.js.
// This is a deterministic lexical screening stage, NOT a trained semantic classifier.
const fs = require("node:fs");
const path = require("node:path");
const RUN_DIR = path.resolve(__dirname,"..");
const GROUP_TERMS = {
  "waterways_and_water": "water waters waterway waterways river rivers stream streams creek creeks lake lakes ocean oceans seas sea groundwater drainage waterfall flood floods flooding canal canals reservoir reservoirs wetlands swamp swamps hydrology turbulence coastal shore shores",
  "settlements_and_places": "city cities town towns village villages urban rural countryside suburbs suburb downtown municipal municipality residents district districts neighborhood neighbourhood neighborhoods neighbourhoods counties county borough settlement settlements communities community locality landscape terrain valley valleys",
  "built_structures": "bridge bridges building buildings house houses housing street streets courtyard courtyards doorway doorways hallway hallways corridor corridors tunnel tunnels staircase staircases stairs palace palaces castle castles architecture architectural infrastructure construction fortress fortresses church churches roofs roof porch porches apartment apartments museum museums hotels hotel gardens garden shelter shelters",
  "transport_and_movement": "transport transported transporting transportation traverse traversing travel traveling travelling travelled traveled traffic crossing cross crosses road roads roadway roadways highway highways rail railway railways train trains wagon wagons route routes routed routing path paths pathway pathways navigation vehicle vehicles airport airports airplane airplanes ship ships trucks truck bus buses transit journey journeys passage mobility movement movements approach approaches access connection connections connect connects connecting connected link links linking linked flow flows",
  "construction_and_engineering": "engineer engineers engineering engineered construct constructed construction contractor contractors builders builder build built materials material steel concrete beams beam foundation foundations design designs designed structure structures structural architect architects mechanical mechanics machinery installation installing installed assembly assembling manufacturing infrastructure",
  "nature_and_ecology": "wilderness forest forests woods trees tree grass swamp swamps bushes bush rocks rock mountain mountains ridge ridges hill hills vegetation plants plant jungle jungles peninsula island islands ecology ecological environment environmental ecosystems ecosystem terrain scenery coastal",
  "scholarship_and_knowledge": "scholar scholars scholarly knowledge knowledgeable academics academic professor professors professionals professional scientist scientists science reasoning rationale research researchers researcher studies study university universities professions expertise philosophy philosophical theology theological ologist ologists scholastic inference inferences analyses analysis interpretation interpretations",
  "evaluation_and_intensity": "intriguing fascinating remarkable remarkably mysterious noteworthy prominent invaluable extraordinary extraordinarily immensely considerable considerably vastly exceptionally largely extensively dramatically magnificent astonishing incredible incredibly hilarious formidable talented daunting charming splendid glorious unfortunate worthwhile unreliable excellent crucial important similar comparable analogous enticing delightful admirable soothing cumbersome horrific wonderful ridiculous pathetic ironic mindful",
  "operation_and_control": "regulates regulate regulation regulations regulating inhibit inhibits inhibited inhibition activate activates activated activation destroy destroys destroyed destruction reduce reduces reduced reduction enhance enhances enhanced inactivation interrupt interrupted shutdown switch switches switched reset flipped flip initialize initialise send execute executes enter entered forwarded transfers transfer purchase purchased installation installing injections",
  "measurement_and_change": "measure measures measured measurement measurements transformation transformations transform transforms transformed changes change alteration alterations movements movement variables variable iterations iteration segments segment transitions transition recording recordings monitoring evaluation evaluations assessing assessment process processes procedure procedures modification modifications experiments experiment comparison comparisons calculations calculation analyses analysed data sensor sensors camera cameras tracking calibration",
  "biology_and_medicine": "cell cells fibroblasts fibroblast lymphocyte lymphocytes macrophages macrophage leukocytes plasmid plasmids transcription transfected cloned clones mutants disease diseases syndrome syndromes pneumonia therapy therapies medications medication drugs drug symptoms symptom kidney lungs lung microglia cytoskeleton cytometry assays assay muscle protein proteins neurodegenerative adrenal cardiovascular neuron neurons genes genetics genetic diagnosis surgery antioxidant enzymes antibodies biological biology",
  "software_and_computing": "python javascript java linux ubuntu windows server servers computer computers laptop laptops database databases adapter adapters configuration config xml json github microsoft google facebook twitter software hardware programming boolean bool classes class function functions token tokens pixels bytes cache processor memory systems status button buttons compiler kernel package packets network networks",
  "clothing_and_equipment": "jacket jackets straps strap sweater sweaters shirt shirts helmet helmets collar collars garments garment blankets blanket coils coil wires wire rods rod shoes shoe sleeve sleeves belt belts bags bag skirt skirts necklace necklaces gloves glove armor armour equipment",
  "food_and_animals": "potatoes potato tomatoes tomato spinach cattle peppers pepper lettuce noodles cakes cake berries berry carrots carrot beans bean chickens chicken eggs egg animals animal dog dogs tiger tigers turtle turtles salmon shrimp worms worm fish fishes sheep cow cows crops mushrooms mushroom food foods vegetables vegetable",
  "competitive_sport": "football basketball baseball hockey soccer quarterback touchdowns touchdown tournament tournaments sport sports championship championships stadium stadiums fielder fielders pitchers pitcher league leagues finals competition competitions racing jets raiders packers puck goal goals team teams",
  "people_and_names": "mitchell molly nina robinson mike sarah brooks lindsay josh jimmy jane helen david stephen richard richardson doug jenkins curtis nelson willie reynolds maggie chris andrew susan matt jim steve johnson garrett powell simmons barry robert george brian thomas",
  "military_and_conflict": "gun guns rifle rifles weapon weapons soldiers soldier troops troop missiles missile terrorists terrorist war wars battle battles army armies combat military handgun handguns bombers bomber rockets rocket attack attacks warfare enemies enemy nazis",
  "juridical_and_crime": "murder murders murdered killings shootings kidnapping lawsuits lawsuit litigation prosecutors prosecutor law laws legislation judiciary offenses crime crimes criminal court courts defendants defendant plaintiffs appellants appellees sheriff police cops officers regulations",
  "belief_and_religion": "theological theology religion religious biblical bible divine god gods church churches heavens heaven jesus christ spiritual christianity philosophical morality faith salvation prayer ritual myth mythology",
  "places_and_countries": "venezuela singapore germany russia switzerland iceland hungary ireland libya atlanta nashville philadelphia pittsburgh boston seattle chicago springfield toronto istanbul texas california paris london tokyo bangkok sydney florida manila tehran portland memphis vancouver dubai kerala"
};
const analyse=function analyse(main,control,terms) {
  const tokens=Object.fromEntries(Object.entries(terms).map(([k,v])=>[k,new Set(v.split(/\s+/).filter(Boolean))]));
  const norm=t=>String(t).replace(/^␠/,"").trim().toLowerCase();
  const group=(c)=>{
    let out=[];
    for(const [label,terms] of Object.entries(tokens)){
      let rep=[...new Set(c.representative_tokens.map(norm).filter(t=>terms.has(t)))];
      let ex=[...new Set(c.most_extreme_tokens.map(norm).filter(t=>terms.has(t)&&!rep.includes(t)))];
      let score=rep.length+0.25*ex.length;
      if(rep.length>=2 && score>=2.5)out.push({label,score,rep,ex});
    }
    out.sort((a,b)=>b.score-a.score||a.label.localeCompare(b.label));
    let total=c.community_size;
    const classcounts=c.token_class_counts||{};
    const punct=(classcounts.punctuation||0)/total;
    const nonword=c.representative_tokens.filter(t=>!/^[␠]?[a-zA-Z]{4,}$/.test(t)).length/c.representative_tokens.length;
    let typ=(punct>=.65)?"punctuation_or_formatting":(nonword>=.70)?"fragment_mixed_script_or_numeric":"not_resolved_by_lexicon";
    if(out.length)typ="candidate_semantic";
    const mixed=out.length>=2&&out[1].score>=out[0].score-0.75;
    return {label:!out.length?null:(mixed?"mixed":out[0].label),
      type:out.length?(mixed?"competing_parent_labels":"candidate_semantic"):typ,
      strength:out.length?+out[0].score.toFixed(2):0,
      labels:out.slice(0,3).map(v=>({label:v.label,strength:+v.score.toFixed(2),matching_representatives:v.rep,matching_extremes:v.ex})),
      rep_correlation:out.length?out[0].rep.length:0}
  };
  const all=[],cells=[],stats={},edgeMap=new Map(),byKey=new Map();
  const initial=()=>({communities:0,classified:0,mixed:0,unresolved:0,punctuation:0,fragment:0,categoryCount:{},categories:{}});
  for(const n of main.networks){
    const stat=initial(), cs=[],cmap=new Map();
    for(const c of n.communities){
      const x=group(c);
      const label=x.label||x.type;
      stat.communities++;
      if(x.label==="mixed")stat.mixed++;
      else if(x.label)stat.classified++;
      else {stat.unresolved++;if(x.type==="punctuation_or_formatting")stat.punctuation++;if(x.type==="fragment_mixed_script_or_numeric")stat.fragment++;}
      stat.categoryCount[label]=(stat.categoryCount[label]||0)+1;
      if(x.label&&x.label!=="mixed")stat.categories[x.label]=(stat.categories[x.label]||0)+c.community_size;
      const row={decision_index:n.decision_index,generated_token_index:n.generated_token_index,state_index:n.state_index,state_label:n.state_label,side:n.side,community_id:c.community_id,
        size:c.community_size,internal_edge_count:c.internal_edge_count,boundary_edge_count:c.boundary_edge_count,
        mean_target_cosine:c.mean_target_cosine,
        candidate_label:x.label,classification:x.type,strength:x.strength,candidate_labels:x.labels,
        representatives:c.representative_tokens,most_extreme:c.most_extreme_tokens};
      cs.push(row);all.push(row);cmap.set(c.community_id,row);
    }
    const cell={decision_index:n.decision_index,generated_token_index:n.generated_token_index,state_index:n.state_index,state_label:n.state_label,side:n.side,...stat,
      candidate_communities:cs.filter(c=>c.candidate_label&&c.candidate_label!=="mixed").sort((a,b)=>b.size-a.size).map(c=>({community_id:c.community_id,label:c.candidate_label,size:c.size,strength:c.strength,representatives:c.representatives.slice(0,9)})),
      unresolved_examples:cs.filter(c=>!c.candidate_label).sort((a,b)=>b.size-a.size).slice(0,3).map(c=>({community_id:c.community_id,size:c.size,type:c.classification,representatives:c.representatives.slice(0,9)}))
    };
    const key=n.decision_index+"|"+n.state_index+"|"+n.side;
    byKey.set(key,{n,rows:cs});cells.push(cell);
    for(const e of n.intercommunity_edges){
      const a=cmap.get(e.community_a),b=cmap.get(e.community_b);
      if(!a?.candidate_label||!b?.candidate_label||a.candidate_label==="mixed"||b.candidate_label==="mixed"||a.candidate_label===b.candidate_label)continue;
      const pair=[a.candidate_label,b.candidate_label].sort().join(" ↔ "),k=n.state_index+"|"+n.side+"|"+pair;
      if(!edgeMap.has(k))edgeMap.set(k,{state_index:n.state_index,side:n.side,pair,decisions:new Set(),count:0,total_token_edges:0,evidence:[]});
      const v=edgeMap.get(k);v.count++;v.total_token_edges+=e.token_edge_count;v.decisions.add(n.decision_index);
      if(v.evidence.length<5)v.evidence.push({decision_index:n.decision_index,communities:[a.community_id,b.community_id],token_edge_count:e.token_edge_count,mean_cosine_similarity:e.mean_cosine_similarity});
    }
  }
  const adjacency={layer:[],generation:[]};
  function match(a,b){
    const src=a.rows.filter(c=>c.candidate_label&&c.candidate_label!=="mixed"), dst=b.rows.filter(c=>c.candidate_label&&c.candidate_label!=="mixed");
    let matches=[],srep=a.n.communities,trep=b.n.communities;
    const tgt=new Map(trep.map(c=>[c.community_id,c]));
    for(const f of src){
      let sc=srep.find(c=>c.community_id===f.community_id);
      let best=null;
      for(const t of dst){if(t.candidate_label!==f.candidate_label)continue;
        let tc=tgt.get(t.community_id);
        let ids=new Set(sc.representative_token_ids), n=tc.representative_token_ids.filter(id=>ids.has(id)).length;
        const overlap=n/Math.max(1,ids.size+tc.representative_token_ids.length-n);
        if(!best||overlap>best.overlap)best={target:t.community_id,overlap,shared_representatives:n};
      }
      if(best&&best.shared_representatives>=3)matches.push({label:f.candidate_label,source:f.community_id,...best});
    }
    return matches;
  }
  for(const n of main.networks){
    const k=n.decision_index+"|"+n.state_index+"|"+n.side;
    if(n.state_index<7){const a=byKey.get(k),b=byKey.get(n.decision_index+"|"+(n.state_index+1)+"|"+n.side);const matches=match(a,b);
      adjacency.layer.push({decision_index:n.decision_index,source_state:n.state_index,target_state:n.state_index+1,side:n.side,matches});}
    if(n.decision_index<31){const a=byKey.get(k),b=byKey.get((n.decision_index+1)+"|"+n.state_index+"|"+n.side);const matches=match(a,b);
      adjacency.generation.push({source_decision:n.decision_index,target_decision:n.decision_index+1,state_index:n.state_index,side:n.side,matches});}
  }
  const contrast={main:{},shuffled:{},shuffled_examples:[]};
  for(const [name,d] of [["main",main],["shuffled",control]]){
    const sum={all:0,labeled:0,mixed:0,per_state:{},per_category:{}};
    for(const n of d.networks){
      let s=sum.per_state[n.state_index]??={all:0,labeled:0,mixed:0};
      for(const c of n.communities){const x=group(c);sum.all++;s.all++;
        if(x.label==="mixed"){sum.mixed++;s.mixed++;}
        else if(x.label){sum.labeled++;s.labeled++;sum.per_category[x.label]=(sum.per_category[x.label]||0)+1;}
        if(name==="shuffled"&&x.label&&contrast.shuffled_examples.length<8)contrast.shuffled_examples.push({d:n.decision_index,s:n.state_index,side:n.side,c:c.community_id,label:x.label,words:c.representative_tokens});}
    }contrast[name]=sum;
  }
  const category=Object.keys(terms);
  const byState=Object.fromEntries(Array.from({length:8},(_,state)=>[state,{state_index:state,communities:0,counts:Object.fromEntries(category.map(x=>[x,0])),decisions:Object.fromEntries(category.map(x=>[x,new Set()])),sides:{positive_head:{},negative_tail:{}}}]));
  const byDecision=Object.fromEntries(Array.from({length:32},(_,d)=>[d,{decision_index:d,states:Object.fromEntries(Array.from({length:8},(_,s)=>[s,{}])),categories:{}}]));
  for(const cell of cells){const st=byState[cell.state_index];st.communities+=cell.communities;for(const [name,c] of Object.entries(cell.categoryCount)){if(!category.includes(name))continue;st.counts[name]+=c;st.decisions[name].add(cell.decision_index);st.sides[cell.side][name]=(st.sides[cell.side][name]||0)+c;
    let dt=byDecision[cell.decision_index];dt.categories[name]=(dt.categories[name]||0)+c;dt.states[cell.state_index][name]=(dt.states[cell.state_index][name]||0)+c;}}
  for(const v of Object.values(byState)) for(const k of category) v.decisions[k]=v.decisions[k].size;
  const edges=[...edgeMap.values()].map(x=>({...x,distinct_decisions:x.decisions.size,decisions:[...x.decisions]})).sort((a,b)=>b.distinct_decisions-a.distinct_decisions||b.total_token_edges-a.total_token_edges);
  const ts=(pairs,axis)=>{
    const out=[];
    for(let state=0;state<8;state++)for(const side of ["positive_head","negative_tail"]){
      const a=pairs.filter(x=>(axis==="generation"?x.state_index:x.source_state_index)===state && x.side===side);
      if(!a.length)continue;
      const avg=k=>a.reduce((t,x)=>t+x[k],0)/a.length;
      out.push({state_index:state,side,pairs:a.length,mean_membership_jaccard:avg("membership_jaccard"),mean_edge_jaccard:avg("edge_jaccard"),min_membership_jaccard:Math.min(...a.map(x=>x.membership_jaccard)),mean_community_ARI:avg("community_adjusted_rand")});
    }return out;
  };
  return {version:1,run_id:main.run_id,generated_analyst_method:"explicit post-hoc phrase lexicon applied identically to original/shuffled representative tokens; provisional candidate labels only, no semantic ground truth",taxonomy_terms:terms,
    summary:{community_count:all.length,network_count:main.networks.length,by_state:byState,by_decision:byDecision,control_contrast:contrast,
      parent_edges:edges,transition_metrics:{across_generation:ts(main.across_decision_generation_transitions,"generation"),within_depth:ts(main.within_decision_state_transitions,"depth")}},
    cells,community_records:all,matches:adjacency};
};
const orig=JSON.parse(fs.readFileSync(path.join(RUN_DIR,"chatgpt_community_networks.json"),"utf8"));
const control=JSON.parse(fs.readFileSync(path.join(RUN_DIR,"controls/shuffled_chatgpt_community_networks.json"),"utf8"));
const result=analyse(orig,control,GROUP_TERMS);
if(result.community_records.length!==6944||result.cells.length!==512)throw Error("Unexpected R020 coverage");
const out=path.resolve(__dirname);
fs.writeFileSync(path.join(out,"R020_DERIVED_DIAGNOSTICS.json"),JSON.stringify({...result,community_records:undefined,cells:undefined,matches:undefined},null,2)+"\n");
fs.writeFileSync(path.join(out,"R020_STATE_CELLS.json"),JSON.stringify({cells:result.cells,matches:result.matches},null,2)+"\n");
for(let k=0;k<4;k++)fs.writeFileSync(path.join(out,`R020_COMMUNITIES_${String(k*8+1).padStart(2,"0")}-${String(k*8+8).padStart(2,"0")}.json`),JSON.stringify({records:result.community_records.filter(x=>x.decision_index>=k*8&&x.decision_index<(k+1)*8)},null,2)+"\n");
