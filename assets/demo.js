const CASES={
 traffic:{
  user:{en:"I got a speed-camera fine, but I wasn't the one driving my car that day.",es:"Me llegó una fotomulta, pero ese día yo no iba manejando mi carro."},
  ack:{en:"Got it, an automated-detection fine (fotomulta). Two quick questions: when did the notice reach you, and do you know who was driving?",es:"Entendido, una fotomulta. Dos preguntas rápidas: ¿cuándo te llegó la notificación y sabes quién iba manejando?"},
  opts:{en:["Last week · I lent it to a friend","A month ago · I don't know"],es:["La semana pasada · se lo presté a un amigo","Hace un mes · no sé quién"]},
  sources:[["Ley 769 de 2002","Código Nacional de Tránsito",94],["Ley 1843 de 2017","Sistemas de fotodetección",91],["Sentencia C-038 de 2020","Corte Constitucional · no automatic owner liability",88]],
  type:{en:"Traffic · automated-detection fine",es:"Tránsito · fotomulta"},
  rule:{en:"The Constitutional Court ruled the owner is not automatically liable for a camera fine: the infraction must be attributed to the person driving.",es:"La Corte Constitucional estableció que el propietario no responde automáticamente por la fotomulta: la infracción debe atribuirse a quien conducía."},
  cites:["Ley 1843/2017","C-038/2020"],
  steps:{en:["Look up the fine on SIMIT and note the notification date.","Request a hearing (audiencia de impugnación) at the transit office that issued it, within the term stated in the notice.","Explain you weren't driving and identify the driver if you can."],es:["Consulta la multa en el SIMIT y anota la fecha de notificación.","Solicita la audiencia de impugnación ante el organismo de tránsito que la impuso, dentro del plazo indicado en la notificación.","Explica que no conducías e identifica al conductor si puedes."]},
  entity:{en:"Transit authority (Secretaría de Movilidad) that issued the fine",es:"Organismo de tránsito (Secretaría de Movilidad) que impuso la multa"},
  docs:{en:["Notice / comparendo","ID card","Vehicle registration (licencia de tránsito)","Proof of where you were"],es:["Notificación / comparendo","Cédula","Licencia de tránsito","Prueba de dónde estabas"]},
  need:"lo", lawyer:{en:"Traffic & administrative law",es:"Derecho de tránsito y administrativo"}
 },
 charge:{
  user:{en:"My phone company keeps charging me for a plan I already cancelled.",es:"Mi operador de celular me sigue cobrando un plan que ya cancelé."},
  ack:{en:"That sounds like an improper charge by a telecom operator. Did you already file a complaint (PQR) with them?",es:"Parece un cobro indebido de un operador de telecomunicaciones. ¿Ya radicaste una queja (PQR) ante ellos?"},
  opts:{en:["Yes, 20 business days ago, no reply","Not yet"],es:["Sí, hace 20 días hábiles y no responden","Todavía no"]},
  sources:[["Ley 1341 de 2009","Régimen TIC · user rights",93],["Res. CRC 5111 de 2017","Régimen de protección de usuarios",92],["Ley 1480 de 2011","Estatuto del Consumidor",84]],
  type:{en:"Consumer · telecom improper charge",es:"Consumidor · cobro indebido de telecomunicaciones"},
  rule:{en:"Operators must answer a complaint within 15 business days. If they don't, the answer is presumed in your favour (silencio administrativo positivo).",es:"El operador debe responder la queja en 15 días hábiles. Si no lo hace, se entiende resuelta a tu favor (silencio administrativo positivo)."},
  cites:["Ley 1341/2009","Res. CRC 5111/2017"],
  steps:{en:["File (or locate) your PQR and keep its CUN tracking number.","If 15 business days pass without an answer, claim the positive silence and ask for the refund.","If the operator still refuses, take the case to the SIC."],es:["Radica (o ubica) tu PQR y guarda el número CUN.","Si pasan 15 días hábiles sin respuesta, invoca el silencio positivo y pide la devolución.","Si el operador se niega, lleva el caso a la SIC."]},
  entity:{en:"Operator first; then Superintendencia de Industria y Comercio (SIC)",es:"Primero el operador; luego la Superintendencia de Industria y Comercio (SIC)"},
  docs:{en:["Invoices with the charge","Cancellation proof","PQR with CUN number","ID card"],es:["Facturas con el cobro","Constancia de cancelación","PQR con número CUN","Cédula"]},
  need:"lo", lawyer:{en:"Consumer protection",es:"Protección al consumidor"}
 },
 labor:{
  user:{en:"They fired me without notice and haven't paid my final settlement.",es:"Me despidieron sin aviso y no me han pagado la liquidación."},
  ack:{en:"I'm sorry, let's sort it out. What kind of contract did you have, and did they give you a reason?",es:"Lo siento, vamos a organizarlo. ¿Qué tipo de contrato tenías y te dieron alguna razón?"},
  opts:{en:["Indefinite term · no reason given","Fixed term · they said “restructuring”"],es:["Término indefinido · sin razón","Término fijo · dijeron “reestructuración”"]},
  sources:[["CST art. 64","Indemnización por despido sin justa causa",95],["CST art. 65","Indemnización moratoria",92],["CST art. 488","Prescripción · 3 años",80]],
  type:{en:"Labor · dismissal without just cause",es:"Laboral · despido sin justa causa"},
  rule:{en:"A dismissal without just cause entitles you to compensation, and late payment of your final wages and benefits can add a daily late-payment penalty.",es:"El despido sin justa causa da derecho a indemnización, y el retraso en pagar salarios y prestaciones finales puede sumar una indemnización moratoria diaria."},
  cites:["CST art. 64","CST art. 65"],
  steps:{en:["Ask your employer in writing for the settlement and the termination letter.","Request a conciliation hearing with a labour inspector at the Ministry of Labour.","If there is no agreement, file a labour claim; you have 3 years."],es:["Pide por escrito la liquidación y la carta de terminación.","Solicita audiencia de conciliación ante un inspector del Ministerio del Trabajo.","Si no hay acuerdo, presenta demanda laboral; tienes 3 años."]},
  entity:{en:"Ministerio del Trabajo · labour courts",es:"Ministerio del Trabajo · jueces laborales"},
  docs:{en:["Employment contract","Payslips","Termination letter or messages","Social security records"],es:["Contrato de trabajo","Desprendibles de pago","Carta o mensajes de despido","Planillas de seguridad social"]},
  need:"hi", lawyer:{en:"Labor law",es:"Derecho laboral"}
 },
 lease:{
  user:{en:"I moved out and my landlord won't give back the deposit I paid.",es:"Me fui del apartamento y el arrendador no me devuelve el depósito."},
  ack:{en:"Let's check. Was it a home (residential) lease, and was the deposit paid in cash or by transfer?",es:"Revisemos. ¿Era un arriendo de vivienda y el depósito fue en efectivo o por transferencia?"},
  opts:{en:["Home lease · bank transfer","Shop / office · cash"],es:["Vivienda · transferencia","Local u oficina · efectivo"]},
  sources:[["Ley 820 de 2003, art. 16","Prohibición de depósitos en vivienda urbana",96],["Ley 2220 de 2022","Estatuto de Conciliación",87],["Código Civil art. 1602","Fuerza obligatoria del contrato",79]],
  type:{en:"Civil · residential lease",es:"Civil · arrendamiento de vivienda"},
  rule:{en:"For urban home leases, the law does not allow landlords to demand cash deposits or similar guarantees, so you can ask for the money back.",es:"En arriendos de vivienda urbana la ley no permite exigir depósitos en dinero ni garantías similares, así que puedes pedir que te devuelvan el dinero."},
  cites:["Ley 820/2003 art. 16"],
  steps:{en:["Send the landlord a written request with proof of the payment.","Request a free conciliation at a university legal clinic or conciliation centre.","If it fails, a small-claims case before a municipal civil judge."],es:["Envía al arrendador una solicitud escrita con el soporte del pago.","Pide una conciliación gratuita en un consultorio jurídico o centro de conciliación.","Si fracasa, proceso de mínima cuantía ante juez civil municipal."]},
  entity:{en:"Conciliation centre · municipal civil judge",es:"Centro de conciliación · juez civil municipal"},
  docs:{en:["Lease contract","Proof of deposit payment","Move-out inventory","Messages with the landlord"],es:["Contrato de arrendamiento","Soporte del pago del depósito","Inventario de entrega","Mensajes con el arrendador"]},
  need:"lo", lawyer:{en:"Civil & real-estate law",es:"Derecho civil e inmobiliario"}
 }
};
const UI={
 en:{who:"TEMIS",search:"Searching verified sources",rel:"relevance",brief:"Case brief",type:"Type of problem",rule:"What the law says",steps:"Next steps",entity:"Where to go",docs:"Documents to bring",needHi:"Lawyer recommended",needLo:"Lawyer optional",conn:"Connect with a lawyer",match:"Best match",matchSub:"Illustrative partner · fixed-fee first review · Bogotá",disc:"Simulated demo · initial guidance, not legal advice",unknown:"I couldn't classify that one in this demo. Try a traffic fine, a phone charge, a dismissal or a lease deposit.",consent:"With your consent, your case brief is shared only with this lawyer."},
 es:{who:"TEMIS",search:"Consultando fuentes verificadas",rel:"relevancia",brief:"Ficha del caso",type:"Tipo de problema",rule:"Qué dice la norma",steps:"Pasos a seguir",entity:"A dónde acudir",docs:"Documentos a llevar",needHi:"Se recomienda abogado",needLo:"Abogado opcional",conn:"Conectar con un abogado",match:"Mejor coincidencia",matchSub:"Aliado ilustrativo · primera revisión con tarifa fija · Bogotá",disc:"Demo simulado · orientación inicial, no asesoría legal",unknown:"No pude clasificar ese caso en este demo. Prueba con una multa, un cobro del celular, un despido o un depósito de arriendo.",consent:"Con tu consentimiento, la ficha se comparte solo con este abogado."}
};
(function(){
const feed=document.getElementById('feed'); if(!feed) return;
const beam=document.getElementById('beam'), scales=document.getElementById('scales');
const reduce=window.matchMedia('(prefers-reduced-motion: reduce)').matches;
let current='traffic', runId=0;
const caseNo=String(Math.floor(10000+Math.random()*89999));
const wait=ms=>new Promise(r=>setTimeout(r,ms));
const esc=s=>s.replace(/[&<>"]/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;'}[c]));
const el=h=>{const d=document.createElement('div');d.innerHTML=h.trim();return d.firstChild};
const add=n=>{feed.appendChild(n);feed.scrollTop=feed.scrollHeight;return n};
const L=()=>window.TEMIS_LANG();
function think(on){scales.classList.toggle('thinking',on); if(!on) beam.style.transform='rotate(0deg)';}
async function typing(id,ms){const t=add(el('<div class="typing"><i></i><i></i><i></i></div>'));await wait(ms);t.remove();return id===runId}

async function run(key,animate,userText){
  const id=++runId; current=key;
  document.querySelectorAll('.chips .chip').forEach(b=>b.setAttribute('aria-pressed',b.dataset.case===key));
  const C=CASES[key], l=L(), U=UI[l], A=!!animate&&!reduce;
  feed.innerHTML='';
  add(el(`<div class="msg user">${esc(userText||C.user[l])}</div>`));
  if(A){think(true); if(!await typing(id,900))return;}
  add(el(`<div class="msg bot"><span class="who">TEMIS</span>${C.ack[l]}</div>`));
  const ans=add(el(`<div class="answers">${C.opts[l].map((o,i)=>`<button type="button" class="chip" data-i="${i}">${o}</button>`).join('')}</div>`));
  let pick=0;
  if(A){ pick=await new Promise(res=>ans.querySelectorAll('button').forEach(b=>b.onclick=()=>res(+b.dataset.i))); if(id!==runId)return; }
  ans.remove();
  add(el(`<div class="msg user">${C.opts[l][pick]}</div>`));
  if(A){ if(!await typing(id,700))return; }
  const ret=add(el(`<div class="retrieval"><div class="h"><span>${U.search}</span><span>RAG · ${U.rel}</span></div>${C.sources.map(s=>`<div class="src"><span class="n">${s[0]}</span><span class="bar"><i style="width:${A?0:s[2]}%"></i></span><span class="d">${s[1]}</span></div>`).join('')}</div>`));
  if(A){ await wait(60); ret.querySelectorAll('.bar i').forEach((b,i)=>b.style.width=C.sources[i][2]+'%'); await wait(1300); if(id!==runId)return; }
  add(el(`<div class="brief">
    <div class="bh"><b>${U.brief}</b><span>TMS-2026-${caseNo} · ${new Date().toLocaleDateString(l==='en'?'en-GB':'es-CO')}</span></div>
    <div class="bb">
      <div><div class="k">${U.type}</div><b>${C.type[l]}</b></div>
      <div><div class="k">${U.rule}</div>${C.rule[l]}<div class="tags" style="margin-top:6px">${C.cites.map(c=>`<span class="tag">${c}</span>`).join('')}</div></div>
      <div><div class="k">${U.steps}</div><ol>${C.steps[l].map(s=>`<li>${s}</li>`).join('')}</ol></div>
      <div><div class="k">${U.entity}</div>${C.entity[l]}</div>
      <div><div class="k">${U.docs}</div><div class="tags">${C.docs[l].map(d=>`<span class="pill">${d}</span>`).join('')}</div></div>
    </div>
    <div class="lawyer"><span class="need ${C.need}">${C.need==='hi'?U.needHi:U.needLo}</span><button type="button" class="btn primary sm" id="connect">${U.conn} →</button></div>
  </div>`));
  think(false);
  add(el(`<p class="disclaim">${U.disc}</p>`));
  document.getElementById('connect').onclick=()=>{
    if(document.getElementById('matchcard'))return;
    const m=el(`<div class="match" id="matchcard"><span class="av">${C.lawyer[l].charAt(0)}</span><div><b>${U.match}: ${C.lawyer[l]}</b><small>${U.matchSub}</small><small>${U.consent}</small></div><span class="sc">${C.need==='hi'?94:89}%</span></div>`);
    feed.insertBefore(m,feed.lastChild); feed.scrollTop=feed.scrollHeight;
  };
  if(!A) feed.scrollTop=0;
}
document.querySelectorAll('.chips .chip').forEach(b=>b.addEventListener('click',()=>run(b.dataset.case,true)));
const KEYS={
  traffic:/(multa|fotomulta|tr[aá]nsito|comparendo|c[aá]mara|ticket|fine|speed|traffic|parking|camera|carro|moto)/i,
  charge:/(cobr|factura|operador|celular|plan|internet|banco|tarjeta|charge|bill|phone|bank|telecom|refund)/i,
  labor:/(despid|trabajo|liquidaci|salario|jefe|empleador|fired|job|salary|wage|employer|boss|dismiss)/i,
  lease:/(arriend|arrendador|dep[oó]sito|apartamento|inquilino|lease|landlord|deposit|rent|tenant|apartment)/i
};
document.getElementById('ask').addEventListener('submit',e=>{
  e.preventDefault();
  const inp=document.getElementById('ask-input'), t=inp.value.trim(); if(!t)return;
  const key=Object.keys(KEYS).find(k=>KEYS[k].test(t)); inp.value='';
  if(key) run(key,true,t);
  else{ runId++; feed.innerHTML=''; add(el(`<div class="msg user">${esc(t)}</div>`)); add(el(`<div class="msg bot"><span class="who">TEMIS</span>${UI[L()].unknown}</div>`)); }
});
document.addEventListener('temis:lang',()=>run(current,false));
run('traffic',false);
})();
