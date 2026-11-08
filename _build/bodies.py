def pages(B, SEAL, COLUMNS, ICON):
    I = ICON

    def page_hero(crumb_en, crumb_es, title_en, title_es, lead_en, lead_es):
        return f'''<section class="page-hero">{COLUMNS}<div class="wrap">
<div class="crumbs"><a href="index.html">TEMIS</a> / {B(crumb_en, crumb_es)}</div>
<h1 class="h-xl" style="max-width:16ch">{B(title_en, title_es)}</h1>
<p class="lead">{B(lead_en, lead_es)}</p></div></section>'''

    def cta_band(t_en, t_es, l_en, l_es):
        return f'''<section class="tight"><div class="wrap"><div class="cta-band">{COLUMNS}
<div style="display:grid;gap:12px;position:relative"><span class="eyebrow">TEMIS</span><h2 class="h-lg">{B(t_en, t_es)}</h2><p class="lead">{B(l_en, l_es)}</p></div>
<div class="acts" style="position:relative"><a class="btn gold" href="demo.html">{B("Try the demo","Probar el demo")}</a><a class="btn light" href="contact.html">{B("Contact us","Contáctanos")}</a></div>
</div></div></section>'''

    # ======================= HOME =======================
    home = f'''
<section class="hero"><div class="wrap">
 <div>
  <span class="eyebrow">{B("Virtual legal clinic · Generative AI","Consultorio jurídico virtual · IA generativa")}</span>
  <h1 class="h-xl" style="margin-top:22px">{B("Clear legal guidance when you don't know <em>where to start.</em>","Orientación jurídica clara cuando no sabes <em>por dónde empezar.</em>")}</h1>
  <p class="lead">{B("Tell TEMIS your problem in your own words. It asks what's missing, checks current Colombian law and explains your next steps: where to go and what documents to bring. When your case needs a lawyer, it connects you with one at a fair price.","Cuéntale a TEMIS tu problema con tus propias palabras. Te pregunta lo que falta, consulta la normatividad colombiana vigente y te explica los siguientes pasos: a dónde acudir y qué documentos llevar. Si tu caso necesita un abogado, te conecta con uno a un precio razonable.")}</p>
  <div class="ctas"><a class="btn primary" href="demo.html">{B("Try the demo","Probar el demo")} →</a><a class="btn" href="video.html">▶ {B("Watch the pitch","Ver el video")}</a></div>
  <div class="trust">
   <span>{I['book']}{B("Grounded in Colombian law","Basado en la ley colombiana")}</span>
   <span>{I['user']}{B("Human lawyers in the loop","Abogados humanos en el proceso")}</span>
   <span>{I['shield']}{B("Privacy by design · Ley 1581","Privacidad desde el diseño · Ley 1581")}</span>
  </div>
 </div>
 <div class="mock">
  <div class="phone"><div class="scr">
   <div class="bar" style="color:#fff">{SEAL}<div><b>TEMIS</b><small>{B("Online · sources verified","En línea · fuentes verificadas")}</small></div></div>
   <div class="msgs">
    <div class="bub u">{B("They fired me without notice and haven't paid my final settlement.","Me despidieron sin aviso y no me han pagado la liquidación.")}</div>
    <div class="bub b">{B("I'm sorry, let's sort it out. What kind of contract did you have?","Lo siento, vamos a organizarlo. ¿Qué tipo de contrato tenías?")}</div>
    <div class="bub u">{B("Indefinite term.","Término indefinido.")}</div>
    <div class="bub b">{B("Under the Labor Code (arts. 64 and 65) you may be owed compensation. Here is your plan…","Según el Código Sustantivo del Trabajo (arts. 64 y 65) podrías tener derecho a indemnización. Este es tu plan…")}</div>
   </div>
   <div class="inp">{B("Describe your problem…","Describe tu problema…")}</div>
  </div></div>
  <div class="float-card"><span class="k">{B("Case brief","Ficha del caso")}</span><b>{B("Labor · dismissal","Laboral · despido")}</b>
   <ul><li>{B("Written request","Solicitud escrita")}</li><li>{B("Ministry of Labour","Ministerio del Trabajo")}</li><li>{B("Labor lawyer · 94% match","Abogado laboral · 94%")}</li></ul></div>
  <div class="float-seal" style="color:#fff">{SEAL}</div>
 </div>
</div></section>

<div class="areas"><div class="wrap">
 <div class="area">{I['car']}<b>{B("Traffic fines","Multas de tránsito")}</b><span>{B("Speed cameras, comparendos, hearings","Fotomultas, comparendos, audiencias")}</span></div>
 <div class="area">{I['receipt']}<b>{B("Improper charges","Cobros indebidos")}</b><span>{B("Telecom, banks, stores, services","Operadores, bancos, tiendas, servicios")}</span></div>
 <div class="area">{I['brief']}<b>{B("Labor issues","Problemas laborales")}</b><span>{B("Dismissal, wages, final settlement","Despidos, salarios, liquidación")}</span></div>
 <div class="area">{I['doc']}<b>{B("Contracts","Contratos")}</b><span>{B("Leases, deposits, unpaid services","Arriendos, depósitos, servicios incumplidos")}</span></div>
</div></div>

<section><div class="wrap">
 <div class="sec-head"><span class="eyebrow">{B("The problem","El problema")}</span><h2 class="h-lg">{B("Most legal problems start with four questions nobody answers.","La mayoría de problemas legales empiezan con cuatro preguntas que nadie responde.")}</h2>
 <p class="lead">{B("Legal jargon, scattered information and the cost of a first consultation keep people from finding a reliable path of action.","El lenguaje jurídico, la información dispersa y el costo de una primera consulta impiden encontrar una ruta de acción confiable.")}</p></div>
 <div class="qs">
  <div><b>{B("What kind of problem is it?","¿Qué tipo de problema es?")}</b><span>{B("And which law applies.","Y qué norma aplica.")}</span></div>
  <div><b>{B("Where should I go?","¿A dónde debo acudir?")}</b><span>{B("Which authority or procedure.","Qué autoridad o trámite.")}</span></div>
  <div><b>{B("What do I need?","¿Qué necesito?")}</b><span>{B("Documents, and when a lawyer is needed.","Documentos, y cuándo se necesita abogado.")}</span></div>
  <div><b>{B("How much will it cost?","¿Cuánto me va a costar?")}</b><span>{B("Before I even begin.","Antes siquiera de empezar.")}</span></div>
 </div>
</div></section>

<section class="alt"><div class="wrap">
 <div class="sec-head center"><span class="eyebrow">{B("How TEMIS helps","Cómo ayuda TEMIS")}</span><h2 class="h-lg">{B("Understand. Guide. Connect.","Entender. Orientar. Conectar.")}</h2></div>
 <div class="grid-3">
  <div class="card"><div class="icon-circle">{I['chat']}</div><h3 class="h-md">{B("Understands your story","Entiende tu relato")}</h3><p>{B("Write as you would talk. TEMIS identifies the type of problem and asks only for the facts it needs.","Escribe como hablarías. TEMIS identifica el tipo de problema y pregunta solo los datos que necesita.")}</p></div>
  <div class="card"><div class="icon-circle">{I['book']}</div><h3 class="h-md">{B("Guides with current law","Orienta con la norma vigente")}</h3><p>{B("Every answer cites the law, decree or ruling it relies on: steps, entity and documents.","Cada respuesta cita la ley, el decreto o la sentencia en que se basa: pasos, entidad y documentos.")}</p></div>
  <div class="card"><div class="icon-circle">{I['scale']}</div><h3 class="h-md">{B("Connects you with a lawyer","Te conecta con un abogado")}</h3><p>{B("When representation or defence is needed, TEMIS matches you with a specialised lawyer or partner firm at a fair rate.","Cuando se requiere representación o defensa, TEMIS te conecta con un abogado o bufete aliado especializado a una tarifa razonable.")}</p></div>
 </div>
 <p style="text-align:center;margin-top:40px"><a class="btn" href="solution.html">{B("See how it works","Ver cómo funciona")} →</a></p>
</div></section>

<section class="dark"><div class="wrap">
 <div class="sec-head"><span class="eyebrow">{B("Backed by research","Respaldado por investigación")}</span><h2 class="h-lg" style="color:#fff">{B("Built on evidence, not on assumptions.","Construido sobre evidencia, no sobre supuestos.")}</h2></div>
 <div class="stats">
  <div class="stat"><div class="n">55</div><p>{B("academic, legal and technical sources","fuentes académicas, jurídicas y técnicas")}</p></div>
  <div class="stat"><div class="n">9</div><p>{B("patents reviewed in Colombia, the US, Europe and WIPO","patentes revisadas en Colombia, EE. UU., Europa y OMPI")}</p></div>
  <div class="stat"><div class="n">12</div><p>{B("standards mapped: ISO, IEEE, W3C, IETF, NIST","normas mapeadas: ISO, IEEE, W3C, IETF, NIST")}</p></div>
  <div class="stat"><div class="n">19<sup>×</sup></div><p>{B("growth in GenAI patent families, 2014–2023 (WIPO)","crecimiento de patentes de IA generativa, 2014–2023 (OMPI)")}</p></div>
 </div>
 <p style="margin-top:44px;display:flex;flex-wrap:wrap;gap:12px"><a class="btn light" href="research.html">{B("Explore the research","Explorar la investigación")} →</a><a class="btn gold" href="docs/TEMIS-investigacion.pdf" target="_blank" rel="noopener">{B("Research PDF","PDF de la investigación")} ↓</a></p>
</div></section>

<section><div class="wrap">
 <div class="grid-2" style="align-items:center;gap:56px">
  <a class="player" href="video.html" style="display:block"><div class="poster"><div class="in"><span class="play"><svg width="30" height="30" viewBox="0 0 24 24"><path d="M8 5v14l11-7z" fill="#fff"/></svg></span><span class="t">TEMIS</span><span class="m">Pitch · 1–2 min · English</span></div></div></a>
  <div style="display:grid;gap:18px"><span class="eyebrow">{B("Pitch video","Video pitch")}</span><h2 class="h-lg">{B("Meet TEMIS in under two minutes.","Conoce TEMIS en menos de dos minutos.")}</h2><p class="lead">{B("Our team presents the idea and shows the product working.","Nuestro equipo presenta la idea y muestra el producto funcionando.")}</p><a class="btn primary" href="video.html" style="justify-self:start">▶ {B("Watch the video","Ver el video")}</a></div>
 </div>
</div></section>

<section class="tight" style="padding-top:0"><div class="wrap">
 <div class="split">
  <div class="p"><span class="eyebrow">{B("For people","Para personas")}</span><h3 class="h-lg">{B("Have a legal problem?","¿Tienes un problema legal?")}</h3>
   <ul><li>{B("Initial guidance in plain language","Orientación inicial en lenguaje sencillo")}</li><li>{B("Steps, entity and documents for your case","Pasos, entidad y documentos para tu caso")}</li><li>{B("A lawyer at a fair price when you need one","Un abogado a precio razonable cuando lo necesites")}</li></ul>
   <a class="btn primary" href="contact.html">{B("Get guidance","Recibir orientación")} →</a></div>
  <div class="c"><span class="eyebrow">{B("For firms &amp; institutions","Para bufetes e instituciones")}</span><h3 class="h-lg" style="color:#fff">{B("Partner with TEMIS","Alíate con TEMIS")}</h3>
   <ul><li>{B("Law firms: receive pre-classified cases, with consent","Bufetes: reciban casos ya clasificados, con consentimiento")}</li><li>{B("Universities and legal clinics: scale your outreach","Universidades y consultorios: amplíen su alcance")}</li><li>{B("Insurers, city halls and NGOs: fund access to justice","Aseguradoras, alcaldías y ONG: financien el acceso a la justicia")}</li></ul>
   <a class="btn gold" href="contact.html#companies">{B("Become a partner","Ser aliado")} →</a></div>
 </div>
</div></section>
'''

    # ======================= SOLUTION =======================
    solution = page_hero("Solution", "Solución",
        "A virtual legal clinic that speaks your language.", "Un consultorio jurídico virtual que habla tu idioma.",
        "TEMIS is designed for people who have a legal problem but don't know what to do or where to go. AI does not replace the lawyer or make judicial decisions: it opens the door to legal guidance.",
        "TEMIS está pensado para personas que tienen un problema legal y no saben qué hacer ni a quién acudir. La IA no reemplaza al abogado ni toma decisiones judiciales: abre la puerta a la orientación jurídica.") + f'''

<section><div class="wrap">
 <div class="sec-head center"><span class="eyebrow">{B("How it works","Cómo funciona")}</span><h2 class="h-lg">{B("From your story to a clear next step.","De tu relato a un siguiente paso claro.")}</h2></div>
 <div class="steps">
  <div class="step"><span class="dot">1</span><b>{B("Tell","Cuenta")}</b><small>NLP</small><p>{B("Describe what happened in plain words.","Describe lo que pasó con palabras sencillas.")}</p></div>
  <div class="step"><span class="dot">2</span><b>{B("Clarify","Aclara")}</b><small>{B("Conversational agent","Agente conversacional")}</small><p>{B("TEMIS asks only for the missing facts.","TEMIS pregunta solo los datos que faltan.")}</p></div>
  <div class="step key"><span class="dot">3</span><b>{B("Retrieve","Consulta")}</b><small>LLM + RAG</small><p>{B("It searches verified laws, decrees and rulings.","Busca leyes, decretos y sentencias verificadas.")}</p></div>
  <div class="step"><span class="dot">4</span><b>{B("Guide","Orienta")}</b><small>{B("Generative AI","IA generativa")}</small><p>{B("You get a case brief with steps, entity and documents.","Recibes una ficha con pasos, entidad y documentos.")}</p></div>
  <div class="step"><span class="dot">5</span><b>{B("Connect","Conecta")}</b><small>{B("Recommender","Recomendador")}</small><p>{B("If needed, a specialised lawyer or partner firm.","Si se necesita, un abogado o bufete aliado especializado.")}</p></div>
 </div>
</div></section>

<section class="alt"><div class="wrap">
 <div class="sec-head"><span class="eyebrow">{B("System design","Diseño del sistema")}</span><h2 class="h-lg">{B("Architecture","Arquitectura")}</h2>
 <p class="lead">{B("A conversational agent understands the story, a retrieval engine grounds every answer in verified legal sources, and a recommender routes complex cases to a human lawyer.","Un agente conversacional entiende el relato, un motor de recuperación sustenta cada respuesta en fuentes jurídicas verificadas y un recomendador lleva los casos complejos a un abogado humano.")}</p></div>
 <div class="arch">
  <div class="arch-row">
   <div class="node"><b>{B("Person","Persona")}</b><span>{B("Story in natural language","Relato en lenguaje natural")}</span></div><span class="arr">→</span>
   <div class="node"><b>{B("Conversational agent","Agente conversacional")}</b><span>NLP · {B("context &amp; follow-up questions","contexto y preguntas")}</span></div><span class="arr">→</span>
   <div class="node core"><b>LLM + RAG</b><span>{B("retrieves sources, then writes the answer","recupera fuentes y redacta la respuesta")}</span></div><span class="arr">→</span>
   <div class="node"><b>{B("Case brief","Ficha del caso")}</b><span>{B("rules · steps · entity · documents","normas · pasos · entidad · documentos")}</span></div>
  </div>
  <div class="kb"><span class="k">{B("Vector database","Base vectorial")}</span><span class="pill">{B("Constitution","Constitución")}</span><span class="pill">{B("Laws &amp; codes","Leyes y códigos")}</span><span class="pill">{B("Decrees","Decretos")}</span><span class="pill">{B("Court rulings","Sentencias")}</span><span class="pill">{B("Official entity guides","Guías de entidades oficiales")}</span></div>
  <div class="arch-row" style="grid-template-columns:1fr auto 1fr">
   <div class="node"><b>{B("Recommender system","Sistema de recomendación")}</b><span>{B("type of problem · location · specialty","tipo de problema · ubicación · especialidad")}</span></div><span class="arr">→</span>
   <div class="node core"><b>{B("Lawyer or partner firm","Abogado o bufete aliado")}</b><span>{B("only with the user's consent","solo con consentimiento del usuario")}</span></div>
  </div>
 </div>
</div></section>

<section><div class="wrap">
 <div class="sec-head"><span class="eyebrow">{B("Emerging technology","Tecnología emergente")}</span><h2 class="h-lg">{B("What powers TEMIS","Qué hace funcionar a TEMIS")}</h2></div>
 <div class="tech">
  <div><span class="ab">GenAI</span><h3>{B("Generative AI","IA generativa")} <sup><a href="research.html#ref-2">[2]</a></sup></h3><p>{B("Models that learn the structure of data to generate new content such as text.","Modelos que aprenden la estructura de los datos para generar contenido nuevo, como texto.")}</p><p class="use"><b>TEMIS</b>{B("Writes the guidance in plain language.","Redacta la orientación en lenguaje sencillo.")}</p></div>
  <div><span class="ab">NLP</span><h3>{B("Natural language processing","Procesamiento de lenguaje natural")} <sup><a href="research.html#ref-4">[4]</a></sup></h3><p>{B("Computational processing of syntax, semantics and sentiment.","Procesamiento computacional de sintaxis, semántica y sentimiento.")}</p><p class="use"><b>TEMIS</b>{B("Understands the story and classifies the problem.","Entiende el relato y clasifica el problema.")}</p></div>
  <div><span class="ab">LLM</span><h3>{B("Large language model","Modelo de lenguaje grande")} <sup><a href="research.html#ref-3">[3]</a></sup></h3><p>{B("Transformer-based models that understand instructions and answer coherently.","Modelos basados en transformadores que entienden instrucciones y responden con coherencia.")}</p><p class="use"><b>TEMIS</b>{B("The reasoning engine of each conversation.","El motor de razonamiento de cada conversación.")}</p></div>
  <div><span class="ab">RAG</span><h3>{B("Retrieval-augmented generation","Generación aumentada por recuperación")} <sup><a href="research.html#ref-32">[32]</a></sup></h3><p>{B("Retrieve relevant documents first, then generate the answer citing them.","Primero recupera documentos pertinentes y luego genera la respuesta citándolos.")}</p><p class="use"><b>TEMIS</b>{B("Answers only from verified norms.","Responde solo con normas verificadas.")}</p></div>
  <div><span class="ab">Vector DB</span><h3>{B("Vector database","Base de datos vectorial")} <sup><a href="research.html#ref-6">[6]</a></sup></h3><p>{B("Stores embeddings and finds the passages closest in meaning to a question.","Guarda vectores y encuentra los pasajes más cercanos en significado a una consulta.")}</p><p class="use"><b>TEMIS</b>{B("Memory of laws, decrees and rulings.","Memoria de leyes, decretos y sentencias.")}</p></div>
  <div><span class="ab">RecSys</span><h3>{B("Recommender system","Sistema de recomendación")} <sup><a href="research.html#ref-8">[8]</a></sup></h3><p>{B("Ranks options by their estimated usefulness for a person.","Ordena alternativas según su utilidad estimada para la persona.")}</p><p class="use"><b>TEMIS</b>{B("Picks the right lawyer or firm.","Elige el abogado o bufete adecuado.")}</p></div>
 </div>
</div></section>

<section class="dark"><div class="wrap">
 <div class="grid-2" style="gap:64px;align-items:start">
  <div style="display:grid;gap:18px"><span class="eyebrow">{B("Users &amp; clients","Usuarios y clientes")}</span><h2 class="h-lg" style="color:#fff">{B("Accessible for users. Sustainable as a business.","Accesible para el usuario. Sostenible como negocio.")}</h2>
   <p class="lead">{B("Users: anyone with a legal question or problem, especially people who don't know the procedures or can't pay a traditional consultation upfront.","Usuarios: cualquier persona con una duda o problema jurídico, especialmente quienes desconocen los procedimientos o no pueden pagar de entrada una consulta tradicional.")}</p></div>
  <div class="payers">
   <div class="payer"><span class="ix">A</span><div><b>{B("Users who upgrade","Usuarios que amplían el servicio")}</b><span>{B("Hire a specialised consultation when the case goes further.","Contratan una consulta especializada cuando el caso lo requiere.")}</span></div></div>
   <div class="payer"><span class="ix">B</span><div><b>{B("Lawyers &amp; law firms","Abogados y bufetes")}</b><span>{B("Receive cases already classified and summarised.","Reciben casos ya clasificados y resumidos.")}</span></div></div>
   <div class="payer"><span class="ix">C</span><div><b>{B("Institutions","Instituciones")}</b><span>{B("Universities, insurers, city halls and social organisations fund access to justice.","Universidades, aseguradoras, alcaldías y organizaciones sociales financian el acceso a la justicia.")}</span></div></div>
  </div>
 </div>
</div></section>

<section><div class="wrap">
 <div class="sec-head"><span class="eyebrow">{B("Responsible by design","Responsable por diseño")}</span><h2 class="h-lg">{B("AI guides. A lawyer decides.","La IA orienta. El abogado decide.")}</h2></div>
 <div class="grid-3">
  <div class="guard"><h3>{B("Every answer shows its source","Cada respuesta muestra su fuente")}</h3><p>{B("Guidance is built only from verified norms.","La orientación se construye solo con normas verificadas.")}</p><div class="basis"><span class="tag">RAG</span><span class="tag">NIST AI 600-1</span></div></div>
  <div class="guard"><h3>{B("Your story is yours","Tu relato es tuyo")}</h3><p>{B("Nothing is shared with a lawyer without explicit consent.","Nada se comparte con un abogado sin consentimiento expreso.")}</p><div class="basis"><span class="tag">Ley 1581/2012</span><span class="tag">SIC 002/2024</span></div></div>
  <div class="guard"><h3>{B("Escalates to a human","Escala a un humano")}</h3><p>{B("Representation and defence always go to a licensed lawyer.","La representación y la defensa siempre van a un abogado habilitado.")}</p><div class="basis"><span class="tag">Ley 1123/2007</span><span class="tag">IEEE 7000</span></div></div>
  <div class="guard"><h3>{B("Managed AI risk","Riesgo de IA gestionado")}</h3><p>{B("Continuous evaluation, traceability and security controls.","Evaluación continua, trazabilidad y controles de seguridad.")}</p><div class="basis"><span class="tag">ISO/IEC 42001</span><span class="tag">OWASP LLM</span></div></div>
  <div class="guard"><h3>{B("Secure by default","Seguro por defecto")}</h3><p>{B("Encrypted channel and information-security management.","Canal cifrado y gestión de seguridad de la información.")}</p><div class="basis"><span class="tag">TLS 1.3</span><span class="tag">ISO/IEC 27001</span></div></div>
  <div class="guard"><h3>{B("Made for everyone","Hecho para todos")}</h3><p>{B("Plain language and accessible design.","Lenguaje sencillo y diseño accesible.")}</p><div class="basis"><span class="tag">WCAG 2.2</span></div></div>
 </div>
</div></section>
''' + cta_band("See TEMIS in action.", "Mira TEMIS en acción.", "Try a real-life case in the interactive demo.", "Prueba un caso de la vida real en el demo interactivo.")

    # ======================= DEMO =======================
    demo = page_hero("Demo", "Demo",
        "Try TEMIS with a real-life case.", "Prueba TEMIS con un caso de la vida real.",
        "Pick an example or write your own problem. This demo uses simulated answers to show how the product works.",
        "Elige un ejemplo o escribe tu propio problema. Este demo usa respuestas simuladas para mostrar cómo funciona el producto.") + f'''
<section><div class="wrap"><div class="demo-wrap">
 <div class="howto">
  <span class="eyebrow">{B("What you'll see","Lo que verás")}</span>
  <h2 class="h-md">{B("One conversation, five moves","Una conversación, cinco movimientos")}</h2>
  <ol>
   <li><span>{B("<b>Your story</b> in plain words.","<b>Tu relato</b> con palabras sencillas.")}</span></li>
   <li><span>{B("<b>A follow-up question</b>: pick an answer.","<b>Una pregunta de seguimiento</b>: elige una respuesta.")}</span></li>
   <li><span>{B("<b>Verified sources</b> ranked by relevance (RAG).","<b>Fuentes verificadas</b> ordenadas por relevancia (RAG).")}</span></li>
   <li><span>{B("<b>Your case brief</b>: rule, steps, entity, documents.","<b>Tu ficha del caso</b>: norma, pasos, entidad, documentos.")}</span></li>
   <li><span>{B("<b>Connect with a lawyer</b> when needed.","<b>Conectar con un abogado</b> cuando se necesite.")}</span></li>
  </ol>
  <p class="note">{B("Simulated demo. Initial guidance only, not legal advice.","Demo simulado. Solo orientación inicial, no asesoría legal.")}</p>
 </div>
 <div class="console" id="console">
  <div class="c-head">
   <svg viewBox="0 0 64 64" aria-hidden="true" id="scales"><g fill="none" stroke="#A9844B" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"><path d="M32 22v34M22 58h20"/><g class="beam" id="beam"><path d="M10 22h44"/><path d="M10 22l-6 14h12zM54 22l-6 14h12z"/></g></g><circle cx="32" cy="16" r="4" fill="#A9844B"/></svg>
   <div><b>TEMIS</b><small>{B("Virtual legal clinic","Consultorio jurídico virtual")}</small></div>
   <span class="live">{B("Sources verified","Fuentes verificadas")}</span>
  </div>
  <div class="chips" role="group" aria-label="Example cases">
   <span class="lbl">{B("Pick a case","Elige un caso")}</span>
   <button class="chip" data-case="traffic" type="button">{B("Traffic fine","Multa de tránsito")}</button>
   <button class="chip" data-case="charge" type="button">{B("Improper charge","Cobro indebido")}</button>
   <button class="chip" data-case="labor" type="button">{B("Fired, unpaid","Despido sin pago")}</button>
   <button class="chip" data-case="lease" type="button">{B("Lease deposit","Depósito de arriendo")}</button>
  </div>
  <div class="feed" id="feed" aria-live="polite"></div>
  <form class="ask" id="ask"><input id="ask-input" aria-label="Describe your problem" autocomplete="off" data-ph-en="Describe your problem in your own words…" data-ph-es="Describe tu problema con tus propias palabras…" placeholder="Describe your problem in your own words…"><button type="submit">{B("Send","Enviar")}</button></form>
 </div>
</div></div></section>
''' + cta_band("Want TEMIS for your organisation?", "¿Quieres TEMIS para tu organización?", "Universities, firms and public entities can partner with us.", "Universidades, bufetes y entidades públicas pueden aliarse con nosotros.")

    # ======================= RESEARCH =======================
    def row(cells, cls=''):
        return f'<tr{(" class=" + chr(34) + cls + chr(34)) if cls else ""}>' + ''.join(f'<td>{c}</td>' for c in cells) + '</tr>'
    def th(*h):
        return '<thead><tr>' + ''.join(f'<th>{B(*x)}</th>' for x in h) + '</tr></thead>'
    A = lambda url, txt: f'<a href="{url}" target="_blank" rel="noopener">{txt}</a>'

    articles = [
     (A("https://books.scielo.org/id/6rj47/pdf/torresvillarreal-9789587845617-02.pdf","Astudillo Fernández et al. (2020)")+"<small>Universidad del Rosario [44]</small>", B("Identifies lack of legal knowledge and guidance as Colombian barriers; proposes an AI chatbot.","Identifica la falta de conocimiento y orientación jurídica como barreras colombianas; propone un chatbot con IA."), B("Closest Colombian precedent: intake interview and problem identification.","Antecedente colombiano más cercano: entrevista inicial e identificación del problema.")),
     (A("https://revistas.uninunez.edu.co/ergaomnes/es/article/view/2687","Atencia Vásquez et al. (2026)")+"<small>Erg@omnes [10]</small>", B("“Justo Bolívar” cognitive chatbot for basic legal guidance with privacy by design.","Chatbot cognitivo “Justo Bolívar” para orientación básica con privacidad desde el diseño."), B("Supports automatic guidance, referral and data protection.","Sustenta orientación automática, remisión y protección de datos.")),
     (A("https://doi.org/10.14718/NovumJus.2024.18.3.7","Botero Chica et al. (2024)")+"<small>Novum Jus [11]</small>", B("PretorIA at the Constitutional Court as support, not a substitute for human reasoning.","PretorIA en la Corte Constitucional como apoyo, sin sustituir el razonamiento humano."), B("TEMIS uses official sources and leaves decisions to lawyers.","TEMIS usa fuentes oficiales y deja la decisión al abogado.")),
     (A("https://doi.org/10.47741/17943108.731","Londoño Villarreal (2025)")+"<small>Revista Criminalidad [9]</small>", B("Compliance guide for GenAI legal chatbots in Colombia.","Guía de cumplimiento para chatbots jurídicos con IA generativa en Colombia."), B("Defines data, transparency and accountability requirements.","Define requisitos de datos, transparencia y responsabilidad.")),
     (A("https://doi.org/10.1145/3594536.3595166","Westermann &amp; Benyekhlef (2023)")+"<small>JusticeBot · ICAIL [38]</small>", B("Method for AI tools that help laypeople access justice.","Método para herramientas de IA que ayudan a personas sin formación jurídica."), B("Reference for the guided-question flow.","Referente del flujo de preguntas guiadas.")),
     (A("https://doi.org/10.48550/arXiv.2502.16573","Panchal et al. (2025)")+"<small>LawPal · arXiv [40]</small>", B("RAG-based system for legal accessibility in India.","Sistema basado en RAG para la accesibilidad legal en India."), B("Shows RAG working for citizen legal questions.","Muestra RAG funcionando para preguntas ciudadanas.")),
     (A("https://doi.org/10.1111/jels.12413","Magesh et al. (2025)")+"<small>J. Empirical Legal Studies [42]</small>", B("Measures hallucinations in leading AI legal research tools.","Mide las alucinaciones de herramientas jurídicas con IA."), B("Why every answer cites its source and lawyers review complex cases.","Por qué cada respuesta cita su fuente y un abogado revisa casos complejos.")),
     (A("https://proceedings.neurips.cc/paper/2020/file/6b493230205f780e1bc26945df7481e5-Paper.pdf","Lewis et al. (2020)")+"<small>NeurIPS · RAG [32]</small>", B("Original retrieval-augmented generation paper.","Artículo original de la generación aumentada por recuperación."), B("Technical basis of the Retrieve stage.","Base técnica de la etapa de consulta.")),
    ]
    def st(kind, en, es): return f'<span class="st {kind}">{B(en, es)}</span>'
    patents = [
     (A("https://patents.google.com/patent/US12164547B2/en","US12164547B2"), "AI advisory systems and methods for constitutional guidance<small>KPN Innovations, 2019</small>", st("on","Active US → 2041","Vigente EE. UU. → 2041"), B("<b>Closest to TEMIS:</b> an AI advisor answers, then finds a human advisor.","<b>La más parecida a TEMIS:</b> un asesor de IA responde y luego busca un asesor humano."), 'hl'),
     (A("https://patents.google.com/patent/US11494860B2/en","US11494860B2"), "Search and recommendation tools for attorney selection<small>Clara Analytics, 2018</small>", st("on","Active US → 2040","Vigente EE. UU. → 2040"), B("Recommends lawyers from litigation data, like our recommender.","Recomienda abogados con datos de litigios, como nuestro recomendador."), ''),
     (A("https://patents.google.com/patent/US11003865B1/en","US11003865B1"), "Retrieval-augmented language model pre-training and fine-tuning<small>Google LLC, 2020</small>", st("on","Active US → 2040","Vigente EE. UU. → 2040"), B("Protects one way of training models with retrieval (RAG).","Protege una forma de entrenar modelos con recuperación (RAG)."), ''),
     (A("https://patents.google.com/patent/US9355370B2/en","US9355370B2"), "System and method for generating legal documents<small>iClosings.com (Legal Maven), 2012</small>", st("on","Active US → 2034","Vigente EE. UU. → 2034"), B("Drafts legal documents with ML; TEMIS does not, for now.","Redacta documentos legales con ML; TEMIS no lo hace por ahora."), ''),
     (A("https://patents.google.com/patent/WO2001009781A2/en","WO2001009781A2"), "Method and system for internet delivery of legal services<small>B. L. Lovig, 1999</small>", st("off","Ceased","Cesada"), B("Connects users with lawyers by area and jurisdiction.","Conecta usuarios con abogados por área y jurisdicción."), ''),
     (A("https://patents.google.com/patent/US20020038233A1/en","US20020038233A1"), "Matching professional service providers with consumers<small>LegalMatch.com, 2000</small>", st("off","Abandoned","Abandonada"), B("Matches clients and lawyers through questions.","Empareja clientes y abogados mediante preguntas."), ''),
     (A("https://patents.google.com/patent/EP3308346A1/en","EP3308346A1"), "Obtaining or providing legal services or advice<small>Bellator Pty Ltd, 2015</small>", st("off","Ceased","Cesada"), B("Shares a case summary with lawyers, like our consented hand-off.","Comparte el resumen del caso con abogados, como nuestro envío con consentimiento."), ''),
     (A("https://patents.google.com/patent/CO2022019139A1/es","CO2022019139A1"), "Control de marca personal con inteligencia artificial<small>Tinver S.A.S., 2022</small>", st("co","Colombia","Colombia"), B("Colombian precedent of AI + network + database architecture.","Antecedente colombiano de arquitectura con IA, red y bases de datos."), ''),
     (A("https://patents.google.com/patent/CO2022006693A1/es","CO2022006693A1"), "Sistema experto de reconocimiento del iris con IA<small>V. G. Quintero Toro, 2022</small>", st("co","Colombia","Colombia"), B("Colombian AI expert-system precedent; indirect relation.","Antecedente colombiano de sistema experto con IA; relación indirecta."), ''),
    ]
    standards = [
     (A("https://www.iso.org/standard/74296.html","ISO/IEC 22989:2022"), B("AI concepts and terminology","Conceptos y terminología de IA"), B("Standard vocabulary for definitions","Vocabulario normalizado")),
     (A("https://www.iso.org/standard/74438.html","ISO/IEC 23053:2022"), B("Framework for ML-based AI systems","Marco para sistemas de IA con ML"), B("Data, model, evaluation, operation","Datos, modelo, evaluación, operación")),
     (A("https://www.iso.org/standard/81230.html","ISO/IEC 42001")+" · "+A("https://www.iso.org/standard/77304.html","23894"), B("AI management system and AI risk","Sistema de gestión y riesgo de IA"), B("Roles, controls, continuous improvement","Roles, controles, mejora continua")),
     (A("https://www.iso.org/standard/27001","ISO/IEC 27001")+" · "+A("https://www.iso.org/standard/27701","27701"), B("Information security and privacy","Seguridad de la información y privacidad"), B("Protecting stories and personal data","Protección de relatos y datos personales")),
     (A("https://standards.ieee.org/ieee/7000/6781/","IEEE 7000-2021"), B("Ethical values in system design","Valores éticos en el diseño"), B("Transparency; never replacing the lawyer","Transparencia; no sustituir al abogado")),
     (A("https://www.w3.org/TR/WCAG22/","W3C WCAG 2.2"), B("Web accessibility","Accesibilidad web"), B("Low digital literacy and disabilities","Baja alfabetización digital y discapacidad")),
     (A("https://www.rfc-editor.org/rfc/rfc8446","IETF RFC 8446 · TLS 1.3"), B("Encrypted communications","Cifrado de comunicaciones"), B("Secure user–TEMIS channel","Canal seguro usuario–TEMIS")),
     (A("https://doi.org/10.6028/NIST.AI.100-1","NIST AI RMF 1.0")+" · "+A("https://doi.org/10.6028/NIST.SP.800-145","SP 800-145"), B("AI risk management; cloud definition","Gestión de riesgos de IA; definición de nube"), B("Risk assessment and cloud deployment","Evaluación de riesgos y despliegue en nube")),
     (A("https://www.icontec.org","ICONTEC"), B("Colombia's national standards body","Organismo nacional de normalización"), B("National reference for NTC certification","Referente nacional para NTC")),
    ]
    law = [
     (A("https://www.funcionpublica.gov.co/eva/gestornormativo/norma.php?i=49981","Ley 1581 de 2012"), B("Personal data protection","Protección de datos personales"), B("Consent, purpose, access and deletion","Consentimiento, finalidad, consulta y eliminación")),
     (A("https://sedeelectronica.sic.gov.co/sites/default/files/normativa/Circular%20Externa%20No.%20002%20del%2021%20de%20agosto%20de%202024.pdf","Circular SIC 002 de 2024"), B("Personal data in AI systems","Datos personales en sistemas de IA"), B("Privacy by design, accountability","Privacidad desde el diseño, responsabilidad")),
     (A("https://colaboracion.dnp.gov.co/CDT/Conpes/Econ%C3%B3micos/4144.pdf","CONPES 4144 de 2025"), B("National AI policy","Política Nacional de IA"), B("Responsible adoption and risk management","Adopción responsable y gestión de riesgos")),
     (A("https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.600-1.pdf","NIST AI 600-1"), B("Generative AI risk profile","Perfil de riesgo de IA generativa"), B("Traceability and human review","Trazabilidad y supervisión humana")),
     (A("https://www.funcionpublica.gov.co/eva/gestornormativo/norma.php?i=22962","Ley 1123 de 2007"), B("Lawyers' disciplinary code","Código Disciplinario del Abogado"), B("Clear warnings, escalation to a licensed lawyer","Advertencias claras, escalamiento a abogado habilitado")),
    ]
    def table(head, rows):
        body = ''.join(row(r[:-1] if len(r) == 5 else r, r[-1] if len(r) == 5 else '') for r in rows)
        return f'<div class="tbl"><table>{head}<tbody>{body}</tbody></table></div>'

    research = page_hero("Research", "Investigación",
        "Backed by research, patents and standards.", "Respaldado por investigación, patentes y normas.",
        "Technology surveillance before building: what has been published, what has been patented and which rules TEMIS must meet. Every item links to its source.",
        "Vigilancia tecnológica antes de construir: qué se ha publicado, qué se ha patentado y qué reglas debe cumplir TEMIS. Cada elemento enlaza a su fuente.") + f'''
<section class="tight" style="padding-bottom:0"><div class="wrap"><a class="btn primary" data-dossier href="docs/TEMIS-investigacion.pdf" target="_blank" rel="noopener">{B("Download the research (PDF)","Descargar la investigación (PDF)")} ↓</a></div></section>
<section class="tight"><div class="wrap">
 <div class="stats light">
  <div class="stat"><div class="n">55</div><p>{B("sources cited","fuentes citadas")}</p></div>
  <div class="stat"><div class="n">9</div><p>{B("patents reviewed","patentes revisadas")}</p></div>
  <div class="stat"><div class="n">12</div><p>{B("standards and frameworks","normas y marcos")}</p></div>
  <div class="stat"><div class="n">14k<sup>+</sup></div><p>{B("GenAI patent families in 2023, up from 733 in 2014","familias de patentes de IA generativa en 2023, frente a 733 en 2014")} <sup><a href="#ref-45">[45]</a></sup></p></div>
 </div>
</div></section>

<section class="alt" id="documents"><div class="wrap">
 <div class="sec-head"><span class="eyebrow">{B("Documents","Documentos")}</span><h2 class="h-lg">{B("Technology research documents","Documentos de investigación tecnológica")}</h2></div>
 <div class="docs">
  <a class="doc" data-dossier href="#documents"><span class="k">PDF</span><b>{B("Full research dossier","Documento de investigación completo")}</b><span>{B("Definitions, articles, patents, standards and legal framework.","Definiciones, artículos, patentes, normas y marco legal.")}</span></a>
  <a class="doc" href="#patents"><span class="k">{B("Patents","Patentes")}</span><b>{B("Patent landscape","Panorama de patentes")}</b><span>{B("Nine patents from Colombia, the US, Europe and WIPO.","Nueve patentes de Colombia, EE. UU., Europa y OMPI.")}</span></a>
  <a class="doc" href="solution.html"><span class="k">{B("Design","Diseño")}</span><b>{B("System architecture","Arquitectura del sistema")}</b><span>{B("Pipeline, knowledge base and guardrails.","Flujo, base de conocimiento y salvaguardas.")}</span></a>
 </div>
</div></section>

<section><div class="wrap">
 <div class="tabs" role="tablist" aria-label="Research" id="articles">
  <button class="tab" role="tab" id="t1" aria-controls="p1" aria-selected="true">{B("Articles","Artículos")}<span class="c">8</span></button>
  <button class="tab" role="tab" id="t2" aria-controls="p2" aria-selected="false">{B("Patents","Patentes")}<span class="c">9</span></button>
  <button class="tab" role="tab" id="t3" aria-controls="p3" aria-selected="false">{B("Standards","Normas técnicas")}<span class="c">9</span></button>
  <button class="tab" role="tab" id="t4" aria-controls="p4" aria-selected="false">{B("Colombian framework","Marco colombiano")}<span class="c">5</span></button>
 </div>
 <span id="patents"></span>
 <div class="panel" role="tabpanel" id="p1" aria-labelledby="t1">{table(th(("Study","Estudio"),("Key contribution","Aporte principal"),("What it means for TEMIS","Aplicación en TEMIS")), articles)}</div>
 <div class="panel" role="tabpanel" id="p2" aria-labelledby="t2" hidden>{table(th(("Publication","Publicación"),("Title · holder","Título · titular"),("Status","Estado"),("Relation to TEMIS","Relación con TEMIS")), patents)}</div>
 <div class="panel" role="tabpanel" id="p3" aria-labelledby="t3" hidden>{table(th(("Standard","Norma"),("What it sets","Qué establece"),("Use in TEMIS","Uso en TEMIS")), standards)}</div>
 <div class="panel" role="tabpanel" id="p4" aria-labelledby="t4" hidden>{table(th(("Source","Fuente"),("Requirement","Exigencia"),("Use in TEMIS","Uso en TEMIS")), law)}</div>
</div></section>

<section class="alt"><div class="wrap">
 <div class="sec-head"><span class="eyebrow">{B("Freedom to operate","Libertad de operación")}</span><h2 class="h-lg">{B("Does it already exist?","¿Ya existe?")}</h2><p class="lead">{B("The pieces exist on their own. What is new is putting them together for Colombia.","Las piezas existen por separado. Lo nuevo es unirlas para Colombia.")}</p></div>
 <div class="fto">
  <div class="row"><h3>{B("Does it already exist?","¿Ya existe?")}</h3><p class="f">{B("Partly: lawyer-matching patents since 1999; Google patented a form of RAG; chatbots like LegalApp, Justo Bolívar, JusticeBot and LawPal already run.","En parte: patentes para conectar con abogados desde 1999; Google patentó una forma de RAG; ya funcionan LegalApp, Justo Bolívar, JusticeBot y LawPal.")}</p><p class="m">{B("TEMIS joins answers from official Colombian sources, case classification and a consented hand-off to a lawyer.","TEMIS une respuestas con fuentes oficiales colombianas, clasificación del caso y conexión con abogado con consentimiento.")}</p></div>
  <div class="row"><h3>{B("How active is the field?","¿Qué tan activo es el campo?")}</h3><p class="f">{B("Very: GenAI patent families grew from 733 (2014) to more than 14,000 (2023).","Mucho: las familias de patentes de IA generativa pasaron de 733 (2014) a más de 14 000 (2023).")}</p><p class="m">{B("Repeat the patent search before launch.","Repetir la búsqueda de patentes antes de lanzar.")}</p></div>
  <div class="row"><h3>{B("Can it be patented in Colombia?","¿Se puede patentar en Colombia?")}</h3><p class="f">{B("Hard: Andean Decision 486 does not consider software “as such” an invention.","Difícil: la Decisión 486 no considera invención al software «como tal».")}</p><p class="m">{B("Protect the code by copyright and register the brand with the SIC.","Proteger el código con derecho de autor y registrar la marca ante la SIC.")}</p></div>
  <div class="row"><h3>{B("Conflicts with active patents?","¿Choca con patentes vigentes?")}</h3><p class="f">{B("Patents only apply where granted; the active US ones don't apply in Colombia unless filed here.","Una patente solo vale donde se concede; las vigentes en EE. UU. no aplican en Colombia si no se pidieron aquí.")}</p><p class="m">{B("If TEMIS reaches the US, review them and use licensed RAG tools.","Si TEMIS llega a EE. UU., revisarlas y usar herramientas RAG con licencia.")}</p></div>
  <div class="row"><h3>{B("Brand and technology risks?","¿Riesgos de marca y tecnología?")}</h3><p class="f">{B("“Temis/Themis” is already used in the legal sector; LLM providers have usage terms; known security risks exist.","«Temis/Themis» ya se usa en el sector jurídico; los proveedores de LLM tienen condiciones de uso; hay riesgos de seguridad conocidos.")}</p><p class="m">{B("Search the trademark in SIPI, review licences and follow OWASP.","Buscar la marca en SIPI, revisar licencias y seguir OWASP.")}</p></div>
 </div>
</div></section>

<section id="references"><div class="wrap">
 <div class="sec-head"><span class="eyebrow">{B("References","Referencias")}</span><h2 class="h-lg">{B("All 55 sources","Las 55 fuentes")}</h2></div>
 <div class="refs" id="refs"></div>
</div></section>
'''

    # ======================= VIDEO =======================
    video = page_hero("Video", "Video",
        "Meet TEMIS.", "Conoce TEMIS.",
        "Our team presents the innovation in English and shows the product working.",
        "Nuestro equipo presenta la innovación en inglés y muestra el producto funcionando.") + f'''
<section><div class="wrap">
 <div class="player" data-player style="max-width:1000px;margin:0 auto">
  <a class="poster" data-video-link href="#"><svg class="columns" viewBox="0 0 520 300" aria-hidden="true"></svg><div class="in"><span class="play"><svg width="34" height="34" viewBox="0 0 24 24"><path d="M8 5v14l11-7z" fill="#fff"/></svg></span><span class="t">TEMIS</span><span class="m">Pitch · 1–2 min · English</span><span class="m" data-soon style="color:var(--gold)">{B("Coming soon","Próximamente")}</span></div></a>
 </div>
 <p style="text-align:center;margin-top:22px"><a class="btn" data-video-link href="#">{B("Open on YouTube / Drive","Abrir en YouTube / Drive")} ↗</a></p>
</div></section>

<section class="alt"><div class="wrap">
 <div class="grid-2" style="gap:64px;align-items:start">
  <div style="display:grid;gap:18px"><span class="eyebrow">{B("About the video","Sobre el video")}</span><h2 class="h-lg">{B("Two minutes, one idea, one team.","Dos minutos, una idea, un equipo.")}</h2><p class="lead">{B("The pitch explains the problem, how TEMIS works, who uses it and who pays, and shows the product in action.","El pitch explica el problema, cómo funciona TEMIS, quién lo usa y quién paga, y muestra el producto en acción.")}</p></div>
  <ul class="checks">
   <li>{I['check']}<div><b>{B("1 to 2 minutes","Entre 1 y 2 minutos")}</b><span>{B("Short and to the point.","Corto y al grano.")}</span></div></li>
   <li>{I['check']}<div><b>{B("In English","En inglés")}</b><span>{B("The whole pitch is in English.","Todo el pitch es en inglés.")}</span></div></li>
   <li>{I['check']}<div><b>{B("The whole team","Todo el equipo")}</b><span>Óscar Leonel Peña Báez · Laura Salazar · Rafael Garzon</span></div></li>
   <li>{I['check']}<div><b>{B("Edited, with music, one setting","Con edición, música y un solo ambiente")}</b><span>{B("A single location for a consistent look.","Un solo lugar para una imagen coherente.")}</span></div></li>
   <li>{I['check']}<div><b>{B("The product on screen","El producto en pantalla")}</b><span>{B("Recorded from the interactive demo.","Grabado desde el demo interactivo.")}</span></div></li>
  </ul>
 </div>
</div></section>
''' + cta_band("Try what you saw in the video.", "Prueba lo que viste en el video.", "The demo runs right in your browser.", "El demo funciona directamente en tu navegador.")
    video = video.replace('<svg class="columns" viewBox="0 0 520 300" aria-hidden="true"></svg>', COLUMNS)

    # ======================= CONTACT =======================
    def field(name, en, es, typ='text', full=False, req=True, ph_en='', ph_es=''):
        r = ' required' if req else ''
        ph = f' data-ph-en="{ph_en}" data-ph-es="{ph_es}" placeholder="{ph_en}"' if ph_en else ''
        ctl = f'<textarea id="{name}" name="{name}"{r}{ph}></textarea>' if typ == 'textarea' else f'<input id="{name}" name="{name}" type="{typ}"{r}{ph}>'
        return f'<div class="field{" full" if full else ""}"><label for="{name}">{B(en, es)}</label>{ctl}</div>'
    def select(name, en, es, opts, full=False):
        o = ''.join(f'<option value="{oe}">{oe} / {os}</option>' for oe, os in opts)
        return f'<div class="field{" full" if full else ""}"><label for="{name}">{B(en, es)}</label><select id="{name}" name="{name}">{o}</select></div>'
    def done(kind):
        return f'''<div class="consent"><input type="checkbox" id="c-{kind}" name="consent" required><label for="c-{kind}">{B("I authorise TEMIS to process my data to answer this request, under Ley 1581 de 2012.","Autorizo a TEMIS a tratar mis datos para responder esta solicitud, conforme a la Ley 1581 de 2012.")}</label></div>
<button class="btn primary send" type="submit">{B("Send request","Enviar solicitud")} →</button>
<p class="ok-msg" role="status" hidden><span class="en">Thank you. Your request has been registered and the TEMIS team will contact you.</span><span class="es">Gracias. Tu solicitud quedó registrada y el equipo de TEMIS te contactará.</span></p>'''

    contact = page_hero("Contact", "Contacto",
        "Let's talk.", "Hablemos.",
        "Whether you have a legal problem or represent an organisation that wants to expand access to justice, write to us.",
        "Si tienes un problema legal o representas una organización que quiere ampliar el acceso a la justicia, escríbenos.") + f'''
<section><div class="wrap"><div class="contact-wrap">
 <div style="display:grid;gap:26px">
  <div style="display:grid;gap:14px"><span class="eyebrow">{B("Contact","Contacto")}</span><h2 class="h-lg">{B("Two ways to work with TEMIS","Dos formas de trabajar con TEMIS")}</h2></div>
  <div class="info">
   <div class="item"><div class="icon-circle">{I['user']}</div><div><b>{B("People","Personas")}</b><span>{B("Tell us your case and receive initial guidance or a lawyer referral.","Cuéntanos tu caso y recibe orientación inicial o la remisión a un abogado.")}</span></div></div>
   <div class="item"><div class="icon-circle">{I['brief']}</div><div><b>{B("Companies, firms &amp; institutions","Empresas, bufetes e instituciones")}</b><span>{B("Join the lawyer network, fund access to justice or bring TEMIS to your community.","Únete a la red de abogados, financia el acceso a la justicia o lleva TEMIS a tu comunidad.")}</span></div></div>
   <div class="item"><div class="icon-circle">{I['mail']}</div><div><b>Email</b><span data-email></span></div></div>
   <div class="item"><div class="icon-circle">{I['pin']}</div><div><b>{B("Location","Ubicación")}</b><span>Bogotá D.C., Colombia · Universidad Militar Nueva Granada</span></div></div>
   <div class="item"><div class="icon-circle">{I['clock']}</div><div><b>{B("Response time","Tiempo de respuesta")}</b><span>{B("Within 2 business days.","En máximo 2 días hábiles.")}</span></div></div>
  </div>
 </div>
 <div>
  <div class="aud-tabs" role="tablist" aria-label="Who are you?">
   <button role="tab" id="tab-pe" aria-controls="f-pe" aria-selected="true" type="button">{B("I'm a person","Soy persona")}</button>
   <button role="tab" id="tab-co" aria-controls="f-co" aria-selected="false" type="button">{B("Company / firm","Empresa / bufete")}</button>
  </div>
  <form class="form" id="f-pe" data-kind="person" role="tabpanel" aria-labelledby="tab-pe">
   <div class="fgrid">
    {field("name","Full name","Nombre completo")}
    {field("email","Email","Correo","email")}
    {field("phone","Phone (optional)","Teléfono (opcional)","tel",req=False)}
    {field("city","City","Ciudad")}
    {select("topic","Type of problem","Tipo de problema",[("Traffic","Tránsito"),("Consumer / charges","Consumidor / cobros"),("Labor","Laboral"),("Lease / contract","Arriendo / contrato"),("Other","Otro")],full=True)}
    {field("message","Tell us what happened","Cuéntanos qué pasó","textarea",full=True,ph_en="Write it as you would tell a friend…",ph_es="Escríbelo como se lo contarías a un amigo…")}
    {done("pe")}
   </div>
  </form>
  <form class="form" id="f-co" data-kind="company" role="tabpanel" aria-labelledby="tab-co" hidden>
   <div class="fgrid">
    {field("org","Organisation","Organización")}
    {select("orgtype","Type","Tipo",[("Law firm / lawyer","Bufete / abogado"),("University / legal clinic","Universidad / consultorio jurídico"),("Insurer","Aseguradora"),("City hall / public entity","Alcaldía / entidad pública"),("NGO / social organisation","ONG / organización social")])}
    {field("name","Contact name","Nombre de contacto")}
    {field("role","Role","Cargo")}
    {field("email","Work email","Correo corporativo","email")}
    {field("phone","Phone","Teléfono","tel")}
    {select("interest","Interest","Interés",[("Join the lawyer network","Unirse a la red de abogados"),("Fund or sponsor access","Financiar o patrocinar"),("Pilot in my institution","Piloto en mi institución"),("Other","Otro")],full=True)}
    {field("message","Message","Mensaje","textarea",full=True)}
    {done("co")}
   </div>
  </form>
 </div>
</div></div></section>

<section class="alt"><div class="wrap">
 <div class="sec-head center"><span class="eyebrow">{B("The team","El equipo")}</span><h2 class="h-lg">{B("Who is behind TEMIS","Quiénes están detrás de TEMIS")}</h2></div>
 <div class="team">
  <div class="member"><span class="ini">OP</span><b>Óscar Leonel Peña Báez</b><span>{B("Co-founder · UMNG","Cofundador · UMNG")}</span></div>
  <div class="member"><span class="ini">LS</span><b>Laura Salazar</b><span>{B("Co-founder · UMNG","Cofundadora · UMNG")}</span></div>
  <div class="member"><span class="ini">RG</span><b>Rafael Garzon</b><span>{B("Co-founder · UMNG","Cofundador · UMNG")}</span></div>
 </div>
</div></section>
'''

    import re
    a=contact.index('<form class="form" id="f-co"'); b=contact.index('</form>',a)
    seg=re.sub(r'\b(id|for)="(?!f-co|c-co)([\w-]+)"', r'\1="co-\2"', contact[a:b])
    contact=contact[:a]+seg+contact[b:]
    return [
        ('index.html', 'TEMIS · Virtual legal clinic', home, ''),
        ('solution.html', 'Solution · TEMIS', solution, ''),
        ('demo.html', 'Demo · TEMIS', demo, '<script src="assets/demo.js"></script>'),
        ('research.html', 'Research · TEMIS', research, '<script src="assets/refs.js"></script><script>(function(){var b=document.getElementById("refs");if(b&&window.TEMIS_REFS){var e=function(s){return s.replace(/[&<>"]/g,function(c){return {"&":"&amp;","<":"&lt;",">":"&gt;","\\"":"&quot;"}[c]})};b.innerHTML=TEMIS_REFS.map(function(r){return \'<p id="ref-\'+r[0]+\'"><b>[\'+r[0]+\']</b>\'+e(r[1])+\' <a href="\'+r[2]+\'" target="_blank" rel="noopener">\'+e(r[2].replace(/^https?:\\/\\//,""))+\'</a></p>\'}).join("");if(location.hash.indexOf("#ref-")===0){var t=document.getElementById(location.hash.slice(1));if(t)t.scrollIntoView()}}if(location.hash==="#patents"){document.getElementById("t2").click()}})();</script>'),
        ('video.html', 'Video · TEMIS', video, ''),
        ('contact.html', 'Contact · TEMIS', contact, ''),
    ]
