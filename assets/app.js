/* ================= CONFIG: fill these in ================= */
const TEMIS_CONFIG = {
  VIDEO_URL: "https://www.youtube.com/watch?v=pkRowL3nou4",      // YouTube or Google Drive link of the pitch video
  DOSSIER_URL: "docs/TEMIS-investigacion.pdf",    // research PDF (hosted in this repo)
  CONTACT_EMAIL: ""   // email that receives contact requests
};
/* ========================================================== */

(function(){
  // ----- language -----
  const root=document.documentElement;
  let lang='en';
  try{ lang=localStorage.getItem('temis-lang')||'en'; }catch(e){}
  function setLang(l){
    lang=l; root.lang=l;
    document.querySelectorAll('.lang button').forEach(b=>b.setAttribute('aria-pressed', b.dataset.l===l));
    document.querySelectorAll('[data-ph-en]').forEach(i=>i.placeholder=i.dataset['ph'+(l==='en'?'En':'Es')]);
    try{localStorage.setItem('temis-lang',l)}catch(e){}
    document.dispatchEvent(new CustomEvent('temis:lang',{detail:l}));
  }
  window.TEMIS_LANG=()=>lang;
  document.querySelectorAll('.lang button').forEach(b=>b.addEventListener('click',()=>setLang(b.dataset.l)));
  setLang(lang);

  // ----- mobile menu -----
  const mb=document.querySelector('.menu-btn'), nav=document.querySelector('nav.main');
  if(mb) mb.addEventListener('click',()=>{const o=nav.classList.toggle('open');mb.setAttribute('aria-expanded',o)});

  // ----- video -----
  function embedUrl(u){
    if(!u) return null;
    let m=u.match(/(?:youtu\.be\/|youtube\.com\/(?:watch\?v=|embed\/|shorts\/))([\w-]{11})/);
    if(m) return 'https://www.youtube.com/embed/'+m[1]+'?rel=0';
    m=u.match(/drive\.google\.com\/file\/d\/([\w-]+)/);
    if(m) return 'https://drive.google.com/file/d/'+m[1]+'/preview';
    return null;
  }
  document.querySelectorAll('[data-player]').forEach(p=>{
    const src=embedUrl(TEMIS_CONFIG.VIDEO_URL);
    if(src){ p.innerHTML='<iframe src="'+src+'" title="TEMIS pitch video" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>'; }
  });
  document.querySelectorAll('[data-video-link]').forEach(a=>{
    if(TEMIS_CONFIG.VIDEO_URL){a.href=TEMIS_CONFIG.VIDEO_URL;a.target='_blank';a.rel='noopener';}
  });
  document.querySelectorAll('[data-soon]').forEach(s=>{ if(TEMIS_CONFIG.VIDEO_URL) s.remove(); });
  document.querySelectorAll('[data-dossier]').forEach(a=>{
    if(TEMIS_CONFIG.DOSSIER_URL){a.href=TEMIS_CONFIG.DOSSIER_URL;a.target='_blank';a.rel='noopener';}
  });
  document.querySelectorAll('[data-email]').forEach(s=>{ s.textContent=TEMIS_CONFIG.CONTACT_EMAIL||'contacto · TEMIS'; });

  // ----- generic tabs -----
  document.querySelectorAll('[role="tablist"]').forEach(list=>{
    const tabs=[...list.querySelectorAll('[role="tab"]')];
    tabs.forEach(t=>t.addEventListener('click',()=>{
      tabs.forEach(x=>{x.setAttribute('aria-selected',x===t);document.getElementById(x.getAttribute('aria-controls')).hidden=x!==t;});
    }));
  });
  if(location.hash==='#companies'){const t=document.getElementById('tab-co'); if(t) t.click();}

  // ----- contact forms -----
  document.querySelectorAll('form.form').forEach(f=>{
    f.addEventListener('submit',e=>{
      e.preventDefault();
      const data=new FormData(f), who=f.dataset.kind;
      const lines=[...data.entries()].filter(([k])=>k!=='consent').map(([k,v])=>k+': '+v);
      const ok=f.querySelector('.ok-msg');
      if(TEMIS_CONFIG.CONTACT_EMAIL){
        const subj=encodeURIComponent('TEMIS · '+(who==='company'?'Company / firm':'Person')+' · '+(data.get('name')||''));
        location.href='mailto:'+TEMIS_CONFIG.CONTACT_EMAIL+'?subject='+subj+'&body='+encodeURIComponent(lines.join('\n'));
        ok.querySelector('.en').textContent='Your email app has opened with the request. Send it and the TEMIS team will reply.';
        ok.querySelector('.es').textContent='Se abrió tu correo con la solicitud. Envíala y el equipo de TEMIS te responderá.';
      }
      else{
        ok.querySelector('.en').textContent='Thank you. The contact inbox is being set up; please reach the TEMIS team through the UMNG course forum in the meantime.';
        ok.querySelector('.es').textContent='Gracias. El buzón de contacto se está configurando; mientras tanto, contacta al equipo de TEMIS por el foro del curso en la UMNG.';
      }
      ok.hidden=false;
    });
  });

  // ----- references -----
  const refBox=document.getElementById('refs');
  if(refBox && window.TEMIS_REFS){
    const esc=s=>s.replace(/[&<>"]/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;'}[c]));
    refBox.innerHTML=window.TEMIS_REFS.map(r=>'<p id="ref-'+r[0]+'"><b>['+r[0]+']</b>'+esc(r[1])+' <a href="'+r[2]+'" target="_blank" rel="noopener">'+esc(r[2].replace(/^https?:\/\//,''))+'</a></p>').join('');
  }
})();
