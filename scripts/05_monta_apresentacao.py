"""
05. Gera a apresentação HTML a partir de data/processed/deck.json.

Saída: docs/apresentacao.html
"""
import os, json
from comum import PROC, DOCS

D = json.load(open(os.path.join(PROC, 'deck.json')))

HTML = r"""<!DOCTYPE html>
<html lang="pt-BR">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Brasil 2002 a 2026 | Metodologia, dados e limitações</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Newsreader:opsz,wght@6..72,300;6..72,400;6..72,500&family=IBM+Plex+Sans:wght@300;400;500;600&family=IBM+Plex+Mono:wght@400;500&display=swap" rel="stylesheet">
<style>
:root{
  --ground:#122029; --panel:#182B35; --line:#2A3F4A;
  --ink:#E6E2D8; --mute:#8598A2; --dim:#5E7480;
  --br:#E8A33D; --grp:#6FA8A0; --grp2:#54707E; --warn:#C9604A;
  --serif:"Newsreader",Georgia,serif;
  --sans:"IBM Plex Sans",system-ui,sans-serif;
  --mono:"IBM Plex Mono",ui-monospace,monospace;
}
*{box-sizing:border-box;margin:0;padding:0}
html,body{height:100%}
body{background:var(--ground);color:var(--ink);font-family:var(--sans);font-weight:300;
  -webkit-font-smoothing:antialiased;overflow:hidden}
.deck{height:100vh;width:100vw;position:relative}
.slide{position:absolute;inset:0;padding:5.5vh 6vw 8vh;display:none;
  flex-direction:column;overflow-y:auto;scrollbar-width:thin}
.slide.on{display:flex}
h1{font-family:var(--serif);font-weight:300;font-size:clamp(2.4rem,5.4vw,4.6rem);
  line-height:1.02;letter-spacing:-.02em;max-width:20ch}
h2{font-family:var(--serif);font-weight:300;font-size:clamp(1.7rem,3.3vw,2.9rem);
  line-height:1.08;letter-spacing:-.015em;max-width:26ch;margin-bottom:.5em}
h3{font-family:var(--sans);font-weight:500;font-size:.98rem;letter-spacing:.01em;margin-bottom:.35em}
p,li{font-size:clamp(.92rem,1.32vw,1.08rem);line-height:1.62;max-width:74ch;color:#D3D0C7}
.lede{font-family:var(--serif);font-size:clamp(1.05rem,1.8vw,1.4rem);line-height:1.5;
  color:var(--ink);max-width:52ch;font-weight:300}
.mute{color:var(--mute)}
.num{font-family:var(--mono);font-variant-numeric:tabular-nums}
b,strong{font-weight:600;color:#F1EEE5}

/* year strip motif */
.strip{display:flex;gap:3px;align-items:flex-end;height:22px;margin-bottom:2.6vh}
.strip i{width:9px;height:7px;background:var(--line);display:block;border-radius:1px}
.strip i.hi{background:var(--br);height:16px}
.strip i.mid{background:var(--grp);height:11px}
.strip span{font-family:var(--mono);font-size:.62rem;color:var(--dim);margin-left:10px;
  align-self:center;letter-spacing:.04em}

.body{display:flex;gap:4vw;margin-top:2.4vh;flex-wrap:wrap}
.col{flex:1;min-width:260px}
.stack>*+*{margin-top:1.1em}

ul{list-style:none}
ul.rule li{padding:.62em 0 .62em 1.1em;border-top:1px solid var(--line);position:relative}
ul.rule li:last-child{border-bottom:1px solid var(--line)}
ul.rule li::before{content:"";position:absolute;left:0;top:1.28em;width:4px;height:4px;
  background:var(--grp);border-radius:50%}
ul.rule li.w::before{background:var(--warn)}

table{border-collapse:collapse;width:100%;font-size:.86rem}
th{text-align:left;font-weight:500;color:var(--mute);font-size:.74rem;padding:.5em .7em;
  border-bottom:1px solid var(--line);letter-spacing:.02em}
td{padding:.52em .7em;border-bottom:1px solid rgba(42,63,74,.55);color:#D3D0C7}
td.n{font-family:var(--mono);font-variant-numeric:tabular-nums;text-align:right}
td.good{color:#8FC7A8}
td.bad{color:#DE8A76}
tr.hl td{background:rgba(232,163,61,.07)}

.big{font-family:var(--mono);font-weight:500;font-size:clamp(2rem,4.6vw,3.4rem);
  color:var(--br);line-height:1;letter-spacing:-.02em}
.kv{display:flex;flex-direction:column;gap:.2em}
.kv .lbl{font-size:.76rem;color:var(--mute)}
.grid4{display:grid;grid-template-columns:repeat(auto-fit,minmax(150px,1fr));gap:2.2vw 2.4vw}

.note{border-left:2px solid var(--warn);padding:.15em 0 .15em 1em;color:#CBBDB4;
  font-size:.92rem;line-height:1.55;max-width:62ch}
.ok{border-left-color:var(--grp)}

/* availability grid */
.avail{display:grid;grid-template-columns:auto repeat(23,1fr) auto;gap:3px;align-items:center;
  font-size:.72rem;max-width:960px}
.avail .nm{font-size:.76rem;color:#D3D0C7;padding-right:.7em;white-space:nowrap}
.avail .c{aspect-ratio:1;background:rgba(255,255,255,.055);border-radius:1px;min-height:11px}
.avail .c.f{background:var(--grp)}
.avail .c.f.br{background:var(--br)}
.avail .tot{font-family:var(--mono);font-size:.72rem;color:var(--mute);padding-left:.7em}
.avail .tot.low{color:var(--warn)}

.defs{margin-top:1em;padding-top:.85em;border-top:1px solid var(--line);
  display:grid;grid-template-columns:repeat(auto-fit,minmax(280px,1fr));gap:.5em 2.4em;max-width:1000px}
.defs div{font-size:.79rem;line-height:1.5;color:var(--mute)}
.defs b{font-weight:500;color:#C9C5BB}
.legend{display:flex;gap:1.4em;flex-wrap:wrap;font-size:.76rem;color:var(--mute);margin-top:1em}
.legend b{display:inline-block;width:20px;height:3px;vertical-align:middle;margin-right:.45em;border-radius:2px}

svg{display:block;width:100%;height:auto}
.chartwrap{margin-top:1.2vh}

/* chrome */
.bar{position:fixed;left:0;bottom:0;height:2px;background:var(--br);transition:width .28s ease;z-index:5}
.cnt{position:fixed;right:2.2vw;bottom:2.4vh;font-family:var(--mono);font-size:.72rem;
  color:var(--dim);letter-spacing:.06em;z-index:5}
.eyebrow{font-size:.74rem;color:var(--br);margin-bottom:.9em;letter-spacing:.04em}
a{color:var(--grp)}
:focus-visible{outline:2px solid var(--br);outline-offset:3px}
@media (prefers-reduced-motion:reduce){*{transition:none!important}}
@media (max-width:720px){
  .slide{padding:4vh 6vw 9vh}
  .body{flex-direction:column;gap:2.2vh}
  .avail{font-size:.6rem;gap:2px}
  .avail .nm{font-size:.62rem}
}
</style>
</head>
<body>
<div class="deck" id="deck"></div>
<div class="bar" id="bar"></div>
<div class="cnt" id="cnt"></div>
<script>
const D = __DATA__;
const YRS = []; for(let y=2002;y<=2026;y++) YRS.push(y);

function strip(hiA, hiB, label){
  let s = '<div class="strip">';
  YRS.forEach(y => {
    let c = (hiA && y>=hiA && y<=hiB) ? 'hi' : '';
    s += '<i class="'+c+'"></i>';
  });
  s += '<span>'+(label||'2002 &nbsp;·&nbsp; 2026')+'</span></div>';
  return s;
}

function chart(series, opts){
  opts = opts||{};
  const W=980, H=opts.h||400, ml=54, mr=opts.mr||34, mt=18, mb=34;
  let xs=[], ys=[];
  series.forEach(s => s.data.forEach(p => {xs.push(p[0]); ys.push(p[1]);}));
  const x0=opts.x0||Math.min(...xs), x1=opts.x1||Math.max(...xs);
  let y0 = opts.y0!==undefined?opts.y0:Math.min(...ys), y1 = opts.y1!==undefined?opts.y1:Math.max(...ys);
  const pad=(y1-y0)*0.12; y0-=pad; y1+=pad;
  const X=v=>ml+(v-x0)/(x1-x0)*(W-ml-mr);
  const Y=v=>mt+(1-(v-y0)/(y1-y0))*(H-mt-mb);
  let g='<svg viewBox="0 0 '+W+' '+H+'" role="img" aria-label="'+(opts.alt||'gráfico')+'">';
  // grid
  const ticks = opts.ticks || 4;
  for(let i=0;i<=ticks;i++){
    const v=y0+(y1-y0)*i/ticks, yy=Y(v);
    g+='<line x1="'+ml+'" x2="'+(W-mr)+'" y1="'+yy+'" y2="'+yy+'" stroke="#2A3F4A" stroke-width="1"/>';
    g+='<text x="'+(ml-9)+'" y="'+(yy+4)+'" fill="#5E7480" font-size="12" font-family="IBM Plex Mono" text-anchor="end">'+(Math.abs(v)>=100?Math.round(v):v.toFixed(1))+'</text>';
  }
  // regime shading
  (opts.bands||[]).forEach(b=>{
    g+='<rect x="'+X(b[0])+'" y="'+mt+'" width="'+(X(b[1])-X(b[0]))+'" height="'+(H-mt-mb)+'" fill="#E8A33D" opacity="0.045"/>';
    g+='<text x="'+(X(b[0])+5)+'" y="'+(mt+13)+'" fill="#5E7480" font-size="10.5" font-family="IBM Plex Sans">'+b[2]+'</text>';
  });
  // x labels
  for(let y=x0;y<=x1;y+=(opts.step||4)){
    g+='<text x="'+X(y)+'" y="'+(H-11)+'" fill="#5E7480" font-size="12" font-family="IBM Plex Mono" text-anchor="middle">'+y+'</text>';
  }
  series.forEach(s=>{
    const pts=s.data.filter(p=>p[1]!==null);
    if(!pts.length) return;
    let d=pts.map((p,i)=>(i?'L':'M')+X(p[0]).toFixed(1)+' '+Y(p[1]).toFixed(1)).join(' ');
    g+='<path d="'+d+'" fill="none" stroke="'+s.color+'" stroke-width="'+(s.w||2)+'" stroke-linejoin="round" stroke-linecap="round"'+(s.dash?' stroke-dasharray="5 4"':'')+'/>';
    const last=pts[pts.length-1];
    g+='<circle cx="'+X(last[0])+'" cy="'+Y(last[1])+'" r="3.4" fill="'+s.color+'"/>';
  });
  return g+'</svg>';
}

function ser(obj, color, name, w, dash){
  const data = Object.keys(obj).map(k=>[+k, obj[k]]).filter(p=>p[1]!==null).sort((a,b)=>a[0]-b[0]);
  return {data:data, color:color, name:name, w:w, dash:dash};
}
const BANDS=[[2003,2011,'boom'],[2012,2014,'desacel.'],[2015,2018,'recessão'],[2019,2021,'pandemia'],[2022,2026,'recuper.']];

/* ---------- slides ---------- */
const S=[];

S.push(`
<div class="eyebrow">Especificação metodológica v3.0 · extração de 06/09/2026</div>
<h1>Como mudou a vida dos brasileiros entre 2002 e 2026</h1>
${strip(2002,2026)}
<p class="lede" style="margin-top:2.4vh">Quem capturou o crescimento, quanto do movimento foi compartilhado com países comparáveis, onde o Brasil se diferenciou e a que custo fiscal.</p>
<div class="note ok" style="margin-top:3vh">Este documento apresenta o desenho da análise e a primeira rodada de dados. <b>A análise não está concluída.</b> O que existe hoje é a extração internacional e o mapa do que falta.</div>
`);

S.push(`
<h2>Onde o trabalho está</h2>
<div class="body"><div class="col stack">
<ul class="rule">
<li><b>Etapa 1. Especificação metodológica.</b> <span class="mute">Concluída. Congelada em v3.0, com objeções antecipadas e corte de escopo.</span></li>
<li><b>Etapa 2. Extração internacional (Tier 1).</b> <span class="mute">Parcial. 29 de 30 indicadores do World Bank. Faltam WID, V-Dem, ITUC, UNODC, IMF e OMS.</span></li>
<li class="w"><b>Etapa 3. Extração nacional (Tier 2).</b> <span class="mute">Não iniciada. É onde está toda a desagregação por raça, região e gênero.</span></li>
<li class="w"><b>Etapa 4. Análise e publicação.</b> <span class="mute">Bloqueada por cinco decisões metodológicas abertas.</span></li>
</ul>
</div><div class="col">
<div class="grid4">
<div class="kv"><div class="big num">8.732</div><div class="lbl">observações extraídas</div></div>
<div class="kv"><div class="big num">29/30</div><div class="lbl">indicadores com dado</div></div>
<div class="kv"><div class="big num">12</div><div class="lbl">países comparadores</div></div>
<div class="kv"><div class="big num">0</div><div class="lbl">linhas desagregadas</div></div>
</div>
</div></div>
`);

S.push(`
<h2>Cinco perguntas independentes</h2>
<p style="margin-bottom:1.6vh">Cada uma pode ter resposta diferente. Não há tentativa de unificá-las em narrativa única.</p>
<div class="body"><div class="col">
<ul class="rule">
<li><b>1. O Brasil ficou mais rico?</b> <span class="mute">PIB per capita, produtividade, investimento, emprego</span></li>
<li><b>2. Quem capturou o crescimento?</b> <span class="mute">Gini, renda dos 40% mais pobres, participação do 1%, Palma</span></li>
<li><b>3. A vida da população pobre melhorou?</b> <span class="mute">Pobreza, fome, mortalidade infantil, saneamento, escolaridade</span></li>
</ul>
</div><div class="col">
<ul class="rule">
<li><b>4a. O cidadão ficou mais protegido?</b> <span class="mute">Previdência, transferência de renda, direitos do trabalho</span></li>
<li><b>4b. E mais seguro?</b> <span class="mute">Homicídios, violência policial, encarceramento, direitos civis</span></li>
<li><b>5. Melhor ou pior que países comparáveis?</b> <span class="mute">Desempenho diferencial contra três grupos</span></li>
<li><b>Transversal. A que custo?</b> <span class="mute">Dívida, resultado primário, gasto social</span></li>
</ul>
</div></div>
<div class="note" style="margin-top:2vh">As perguntas 4a e 4b são separadas de propósito. Cobertura previdenciária e taxa de homicídios não são manifestações do mesmo fenômeno.</div>
`);

S.push(`
<h2>A métrica central: desempenho diferencial</h2>
<div class="body"><div class="col stack">
<p style="font-family:var(--mono);font-size:.95rem;color:#E6E2D8;border-left:2px solid var(--br);padding-left:1em;line-height:1.7">
desempenho diferencial =<br>variação do Brasil<br>&minus; variação da mediana do grupo</p>
<p>Se a pobreza extrema cai 8 pontos no Brasil e 7 pontos na mediana dos emergentes, o desempenho diferencial é de 1 ponto. Os dois números são publicados sempre lado a lado.</p>
</div><div class="col">
<h3 style="color:var(--warn)">O que essa métrica não é</h3>
<p>Ela <b>não é um contrafactual</b>. Não permite afirmar que 1 ponto da melhora foi causado por fatores domésticos.</p>
<p style="margin-top:.9em">O diferencial pode refletir composição demográfica, exposição a commodities, severidade do choque, estrutura produtiva, câmbio ou tendência prévia.</p>
<p style="margin-top:.9em" class="mute">A palavra contrafactual fica reservada a análises que construam a trajetória esperada do Brasil na ausência de um choque, o que está fora do escopo.</p>
</div></div>
`);

S.push(`
<h2>Quatro camadas de comparação</h2>
${strip(1995,2001,'camada 0 · trajetória anterior')}
<div class="body"><div class="col">
<ul class="rule">
<li><b>Camada 0. Trajetória interna, 1995 a 2001.</b> <span class="mute">Verifica se o movimento pós 2002 é continuidade, aceleração ou reversão de tendência que já existia. Sem ela, uma queda de mortalidade infantil em curso desde os anos 90 vira excepcionalidade do período.</span></li>
<li><b>Camada A. Série anual.</b> <span class="mute">Unidade básica. Todo gráfico é anual.</span></li>
</ul>
</div><div class="col">
<ul class="rule">
<li><b>Camada B. Regimes econômicos.</b> <span class="mute">Única partição usada para calcular deltas. Definida por condições externas: boom 2003 a 2011, desaceleração 2012 a 2014, recessão 2015 a 2018, pandemia 2019 a 2021, recuperação 2022 a 2026.</span></li>
<li class="w"><b>Camada C. Mandatos. Narrativa apenas.</b> <span class="mute">Sobrepostos à série para contexto. Não recebem cálculo de delta, não recebem atribuição de resultado e não são ranqueados.</span></li>
</ul>
</div></div>
`);

S.push(`
<h2>Dois tiers de dado, sem mistura</h2>
<div class="body"><div class="col stack">
<h3 style="color:var(--grp)">Tier 1 · comparação internacional</h3>
<p>Só bases já harmonizadas entre países. <b>Nenhuma fonte nacional entra aqui, inclusive para o Brasil.</b></p>
<p class="mute" style="font-size:.88rem">World Bank PIP e WDI · ILOSTAT · UNDP · JMP · UNESCO · UNODC · FAO SOFI · WID.world · UN IGME · WHO · IMF WEO · ITUC · V&#8209;Dem · World Prison Brief</p>
</div><div class="col stack">
<h3 style="color:var(--br)">Tier 2 · Brasil em alta resolução</h3>
<p>É aqui que ocorre toda a desagregação por raça, região, gênero e situação do domicílio.</p>
<p class="mute" style="font-size:.88rem">IBGE · DataSUS · INEP · SNIS · CadÚnico · BCB · FBSP · Tesouro · Receita Federal · MTE · SISDEPEN</p>
</div></div>
<div class="note" style="margin-top:2.2vh">O valor do Brasil em qualquer gráfico comparativo vem do Tier 1, <b>mesmo quando difere do valor oficial do IBGE</b>. As séries divergem por definição metodológica. A divergência é documentada uma vez e não é reconciliada.</div>
`);

S.push(`
<h2>Grupos de comparação</h2>
<p style="margin-bottom:1.4vh">Calculados por mediana, não média. Composição congelada antes da extração.</p>
<table>
<tr><th>Grupo</th><th>Composição</th><th>Uso</th></tr>
<tr><td>América Latina</td><td class="mute">México, Colômbia, Chile, Peru, Argentina, Equador</td><td>principal</td></tr>
<tr><td>G20 emergentes</td><td class="mute">Índia, Indonésia, África do Sul, Turquia, China, México</td><td>sempre com e sem China</td></tr>
<tr><td>Emergentes amplo</td><td class="mute">agregado Upper Middle Income do Banco Mundial</td><td>principal</td></tr>
<tr><td>Exportadores de commodities</td><td class="mute">Chile, Colômbia, Peru, África do Sul, Indonésia</td><td>teste de termos de troca</td></tr>
<tr><td>Benchmark de pandemia</td><td class="mute">definido por excesso de mortalidade e dívida sobre PIB em 2019</td><td>2020 e 2021</td></tr>
</table>
<div class="note" style="margin-top:2vh">Os critérios do benchmark de pandemia são exclusivamente numéricos e publicados antes de ver os resultados. Um grupo escolhido por &ldquo;similaridade&rdquo; depois de olhar os dados seria seleção post hoc.</div>
`);

S.push(`
<div class="eyebrow">Mudança de composição</div>
<h2>Índia e África do Sul saem dos indicadores de distribuição</h2>
<div class="body"><div class="col stack">
<p>A Índia tem <span class="num">4</span> anos de Gini e pobreza observados em 22. A África do Sul tem <span class="num">5</span>. Nos dois casos, a mediana do grupo estava sendo formada por interpolação, não por medição.</p>
<p><b>A exclusão é feita por regra, não por nome:</b> um país só entra na mediana de um indicador de distribuição se tiver ao menos <span class="num">10</span> anos observados no período. A regra é aplicada igualmente a todos e vale para qualquer indicador esparso.</p>
<p class="mute">Chile fica no limite, com 10 anos, e permanece. Os grupos de crescimento, emprego e mortalidade não mudam, porque têm série anual completa.</p>
</div><div class="col stack">
<h3 style="color:var(--warn)">O risco que isso cria</h3>
<p>Excluir países depois de ver os resultados é exatamente a manipulação de composição que a metodologia proíbe. E a exclusão <b>mudou o resultado do boom de commodities</b>: a mediana do G20 passou de menos 17,2 para menos 5,9 pontos, e o Brasil deixou de perder e passou a ganhar dessa comparação.</p>
<div class="note">Por isso a regra precisa ser publicada como regra, com o número de anos exigido declarado antes, e as duas versões do resultado precisam aparecer lado a lado na publicação. Sem isso, a mudança é indefensável, por mais correta que seja tecnicamente.</div>
</div></div>
`);

S.push(`
<h2>Pobreza extrema, 2002 a 2024</h2>
<p class="mute" style="font-size:.86rem">% da população abaixo de US$ 3,00 por dia em PPC de 2021, linha revisada pelo Banco Mundial em junho de 2025</p>
<div class="chartwrap">__CH_POV__</div>
<div class="legend" style="margin-top:.8vh">
<span><b style="background:var(--br)"></b>Brasil</span>
<span><b style="background:var(--grp)"></b>Mediana da América Latina</span>
<span><b style="background:var(--grp2)"></b>Mediana do G20 emergentes, sem China</span>
</div>
<p style="margin-top:1.2vh">O Brasil sai de <span class="num">16,2%</span> em 2002 para <span class="num">3,0%</span> em 2024. A mediana latino americana percorre uma trajetória parecida e chega ao mesmo patamar.</p>
<div class="defs">
<div><b>Pobreza extrema.</b> Percentual da população que vive com menos de US$ 3,00 por dia. Renda familiar dividida pelo número de pessoas da casa, medida por pesquisa domiciliar.</div>
<div><b>PPC, paridade do poder de compra.</b> Conversão que ajusta pela diferença de preços entre países, em vez do câmbio de mercado. US$ 1 em PPC compra a mesma cesta em qualquer país. Elimina a distorção da volatilidade do real.</div>
<div><b>Mediana do grupo.</b> Valor do país que fica no meio do grupo naquele ano, não a média. Resiste a distorção causada por um país atípico.</div>
</div>
`);

S.push(`
<h2>Desigualdade e participação da base</h2>
<div class="body"><div class="col">
<h3>Índice de Gini</h3>
<div class="chartwrap">__CH_GINI__</div>
</div><div class="col">
<h3>Participação de renda dos 40% mais pobres (%)</h3>
<div class="chartwrap">__CH_B40__</div>
</div></div>
<div class="legend" style="margin-top:.8vh">
<span><b style="background:var(--br)"></b>Brasil</span>
<span><b style="background:var(--grp)"></b>Mediana da América Latina</span>
<span><b style="background:var(--grp2)"></b>Mediana do G20 emergentes, sem China</span>
</div>
<p style="margin-top:1.2vh">Gini brasileiro cai de <span class="num">58,1</span> para <span class="num">50,3</span>. A queda é contínua até 2014, reverte na recessão e volta a cair a partir de 2021. A mediana do G20 sem China vem de só três países com cobertura suficiente, ver regra de cobertura mínima.</p>
<div class="defs">
<div><b>Índice de Gini.</b> Mede a concentração de renda numa escala de 0 a 100. Zero seria todo mundo ganhando igual, 100 seria uma pessoa com toda a renda. Quanto menor, menos desigual.</div>
<div><b>Participação dos 40% mais pobres.</b> Quanto da renda total do país fica com a metade de baixo menos rica. Se fosse distribuição perfeitamente igual, seriam 40%. É a soma dos dois quintis inferiores.</div>
<div><b>Limite comum aos dois.</b> Pesquisa domiciliar subestima sistematicamente a renda do topo, porque os mais ricos respondem menos e declaram menos. Os dois indicadores precisam ser lidos junto à participação do 1% apurada por dado tributário, ainda não extraída.</div>
</div>
`);

S.push(`
<h2>Renda cresceu. Produtividade, muito menos.</h2>
<p class="mute" style="font-size:.86rem">Índice com base 2002 = 100: cada linha mostra quanto o indicador cresceu desde 2002, não o valor absoluto. Grupos em mediana, país indexado antes de entrar na mediana.</p>
<div class="body"><div class="col">
<h3>PIB per capita em PPC</h3>
<div class="chartwrap">__CH_PIB__</div>
</div><div class="col">
<h3>Produtividade do trabalho</h3>
<div class="chartwrap">__CH_PROD__</div>
</div></div>
<div class="legend" style="margin-top:.8vh">
<span><b style="background:var(--br)"></b>Brasil</span>
<span><b style="background:var(--grp)"></b>Mediana da América Latina</span>
<span><b style="background:var(--grp2)"></b>Mediana do G20 emergentes, sem China</span>
</div>
<p style="margin-top:1.2vh">Em 2025 o PIB per capita brasileiro está em <span class="num">140</span> e a produtividade em <span class="num">125</span>, contra <span class="num">237</span> e <span class="num">205</span> na mediana do G20 sem China. Dividir PIB por produtividade dá exatamente a razão entre pessoas ocupadas e população total: <b>o Brasil produziu mais por habitante em boa parte porque passou a ter proporcionalmente mais gente trabalhando</b>, e não porque cada trabalhador produziu muito mais. Os pares cresceram nas duas frentes.</p>
<div class="defs">
<div><b>PIB per capita em PPC.</b> Produto interno bruto dividido pela população inteira, convertido por paridade do poder de compra e com a inflação removida (dólares internacionais constantes de 2021). Aproxima a renda média por habitante.</div>
<div><b>Produtividade, ou PIB por pessoa ocupada.</b> O mesmo PIB, dividido pelo número de pessoas efetivamente trabalhando em vez de pela população. Mede quanto valor cada trabalhador gera por ano.</div>
<div><b>Por que as duas divergem, no Brasil.</b> A diferença entre elas é, por definição, a mudança na proporção de ocupados sobre a população: mais gente em idade de trabalhar e maior participação da mulher no mercado. É um ganho que acontece uma vez e não se repete.</div>
<div><b>Ressalva do cálculo.</b> A medida é por trabalhador e não por hora trabalhada. Mudanças em jornada média, tempo parcial e informalidade entram no número. Produtividade por hora seria melhor, mas tem cobertura internacional muito pior.</div>
</div>
`);

S.push(`
<h2>Indicadores sociais, mesma base comparativa</h2>
<p class="mute" style="font-size:.86rem">Brasil, mediana da América Latina e mediana do G20 emergentes sem China, quando o indicador tem dado para os três.</p>
<div class="body"><div class="col">
<h3>Mortalidade infantil <span class="mute">por mil nascidos vivos</span></h3>
<div class="chartwrap">__CH_IMR__</div>
<h3 style="margin-top:1.6vh">Homicídios <span class="mute">por 100 mil habitantes</span></h3>
<div class="chartwrap">__CH_HOM__</div>
</div><div class="col">
<h3>Saneamento básico <span class="mute">% da população</span></h3>
<div class="chartwrap">__CH_SAN__</div>
<h3 style="margin-top:1.6vh">Desemprego <span class="mute">% da força de trabalho</span></h3>
<div class="chartwrap">__CH_DES__</div>
</div></div>
<div class="legend" style="margin-top:1.2vh">
<span><b style="background:var(--br)"></b>Brasil</span>
<span><b style="background:var(--grp)"></b>Mediana da América Latina</span>
<span><b style="background:var(--grp2)"></b>Mediana do G20 emergentes, sem China</span>
</div>
<div class="defs">
<div><b>Mortalidade infantil.</b> Mortes de crianças com menos de 1 ano a cada mil nascidas vivas. É o indicador mais sensível a acesso a saúde básica, pré-natal e saneamento.</div>
<div><b>Saneamento básico.</b> Percentual da população com acesso a instalação sanitária de uso próprio que separa o esgoto do contato humano. Definição do JMP, da OMS e do UNICEF.</div>
<div><b>Homicídios.</b> Mortes intencionais causadas por outra pessoa, por 100 mil habitantes. A série aqui é a do UNODC. A leitura completa exige publicar junto as mortes por causa indeterminada, que ainda não foram extraídas.</div>
<div><b>Desemprego.</b> Percentual da força de trabalho que está sem trabalho e procurando. Não inclui desalentados nem subocupados, que entram na taxa de subutilização.</div>
</div>
`);

S.push(`
<h2>Fome: a subida e a descida mais bruscas da série</h2>
<p class="mute" style="font-size:.86rem">Insegurança alimentar moderada ou grave, % da população. Escala FIES da FAO. Série começa em 2015.</p>
<div class="chartwrap">__CH_FOME__</div>
<div class="legend" style="margin-top:.8vh">
<span><b style="background:var(--br)"></b>Brasil</span>
<span><b style="background:var(--grp)"></b>Mediana da América Latina</span>
<span><b style="background:var(--grp2)"></b>Mediana do G20 emergentes, sem China</span>
</div>
<p style="margin-top:1.2vh">O Brasil sobe de <span class="num">13,3%</span> em 2015 para <span class="num">22,1%</span> em 2021 e volta a <span class="num">13,5%</span> em 2023. É a única reversão dessa magnitude no grupo. A mediana latino americana subiu de forma contínua e não voltou.</p>
<div class="defs">
<div><b>Escala FIES.</b> Questionário de oito perguntas aplicado direto às pessoas sobre a experiência recente de falta de comida: pular refeição, comer menos do que precisava, ficar um dia sem comer. Não usa renda como proxy.</div>
<div><b>Moderada ou grave.</b> Inclui desde quem reduziu qualidade e quantidade da comida até quem passou dias sem comer. A categoria só grave é bem menor.</div>
<div><b>Por que importa aqui.</b> É o indicador de bem estar que mais se move no curto prazo. Pobreza monetária e mortalidade demoram anos para reagir; fome reage em meses.</div>
<div><b>Limite da série.</b> Começa em 2015 e não cobre os três primeiros regimes. A mediana do G20 sem China vem só de Indonésia e África do Sul, sem dado para Índia, Turquia e China, então essa linha é a mais fraca do grupo.</div>
</div>
`);

S.push(`
<div class="eyebrow">Resultados preliminares · Tier 1 apenas</div>
<h2>As cinco perguntas, respondidas com o que existe hoje</h2>
<div class="body"><div class="col">
<ul class="rule">
<li><b>1. O Brasil ficou mais rico? Sim, pouco, e menos que os pares.</b> <span class="mute">Renda por habitante mais 43% em 23 anos. América Latina mais 62%, demais emergentes mais 144%. Investimento caiu.</span></li>
<li><b>2. Quem capturou o crescimento? A base.</b> <span class="mute">Gini cai 8,1 pontos, participação dos 40% mais pobres sobe de 8,5% para 12%, participação dos 10% mais ricos cai de 46% para 39%. Distribuição foi progressiva.</span></li>
<li><b>3. A vida dos pobres melhorou? Sim, muito, em quase tudo.</b> <span class="mute">Pobreza extrema de 17,5% para 3%, em 23 anos. Mortalidade infantil cai 55%. Saneamento sobe 18 pontos. Ensino médio completo mais que dobra. Fome é a exceção: volta ao ponto de partida, mas a série só existe de 2015 a 2023, um recorte bem mais curto que os demais.</span></li>
</ul>
</div><div class="col">
<ul class="rule">
<li class="w"><b>4a. O cidadão ficou mais protegido? Não dá para responder.</b> <span class="mute">A série de cobertura de proteção social tem entre 1 e 16 observações por país. Nenhuma fonte de direitos do trabalho foi extraída.</span></li>
<li><b>4b. E mais seguro? Sim, e contra a tendência regional.</b> <span class="mute">Homicídios caem 29%, de 27,2 para 19,3 por 100 mil. A mediana latino americana subiu 98% no mesmo período.</span></li>
<li><b>5. Melhor ou pior que os pares? Depende da dimensão, e essa é a resposta.</b> <span class="mute">Pior em crescimento e produtividade. Melhor em distribuição e segurança. Empatado em pobreza e mortalidade.</span></li>
</ul>
</div></div>
<div class="note" style="margin-top:1.4vh">Todos os números comparam 2002 com o último ano disponível, entre 2023 e 2025 conforme o indicador. <b>São preliminares.</b> Não há desagregação, não há dado tributário de topo, não há fiscal, e a pergunta transversal do custo continua sem resposta.</div>
`);

S.push(`
<div class="eyebrow">Pergunta 1</div>
<h2>O Brasil ficou mais rico?</h2>
<p class="mute" style="font-size:.86rem">Variação absoluta e, entre parênteses, a variação proporcional. Verde é melhora, vermelho é piora.</p>
<div class="chartwrap">__ANS_P1__</div>
<p style="margin-top:1.2vh"><b>Sim, mas pouco e mais devagar que os pares.</b> A renda por habitante subiu 43% em 23 anos, contra 62% da mediana latino americana e 144% dos demais emergentes. A produtividade subiu 25%, contra 115% do grupo emergente. O investimento sobre PIB <b>caiu</b>, enquanto subiu em todos os grupos de comparação.</p>
<div class="defs">
<div><b>O ponto forte.</b> O desemprego caiu 4,7 pontos, redução proporcional muito maior que a dos pares. O Brasil colocou gente para trabalhar.</div>
<div><b>O ponto fraco.</b> Colocou gente para trabalhar sem elevar quanto cada um produz, e investindo uma fatia menor do PIB do que investia em 2002. É a combinação que limita a continuidade do ganho.</div>
</div>
`);

S.push(`
<div class="eyebrow">Pergunta 2</div>
<h2>Quem capturou o crescimento?</h2>
<div class="chartwrap">__ANS_P2__</div>
<p style="margin-top:1.2vh"><b>A base da pirâmide.</b> Os três indicadores apontam na mesma direção: o Gini cai 8,1 pontos, os 40% mais pobres saem de 8,5% para 12% da renda total, e os 10% mais ricos recuam de 46,1% para 39,3%. A América Latina teve movimento parecido; os demais emergentes foram na direção oposta, concentrando renda.</p>
<div class="defs">
<div><b>A ressalva que pode inverter isso.</b> Todos esses números vêm de pesquisa domiciliar, que subestima sistematicamente a renda do topo. A participação do 1% mais rico apurada por dado tributário, que ainda não foi extraída do WID.world, costuma mostrar trajetória bem mais estável. É perfeitamente possível que Gini caia e concentração no topo não mude.</div>
<div><b>Combinada com a pergunta 1.</b> Crescimento fraco com distribuição progressiva. A base ganhou participação num bolo que cresceu devagar.</div>
</div>
`);

S.push(`
<div class="eyebrow">Pergunta 3</div>
<h2>A vida da população pobre melhorou?</h2>
<div class="chartwrap">__ANS_P3__</div>
<p style="margin-top:1.2vh"><b>Sim, e essa é a resposta mais forte da análise.</b> Pobreza extrema cai de 17,5% para 3%. Mortalidade infantil cai 55%, mais que a mediana latino americana. Saneamento avança 18 pontos. A conclusão do ensino médio entre adultos mais que dobra, com avanço muito maior que o dos dois grupos.</p>
<div class="defs">
<div><b>A exceção.</b> Insegurança alimentar termina em 13,5%, praticamente onde começou em 2015, depois de chegar a 22,1% em 2021. O nível é o mesmo, mas a trajetória não foi plana. A mediana latino americana piorou 50% no mesmo intervalo, então o desempenho relativo brasileiro é bom mesmo com resultado absoluto estagnado.</div>
<div><b>O que falta para fechar.</b> Sem a desagregação do Tier 2 não se sabe se esse avanço foi homogêneo. É improvável que tenha sido, e a diferença entre Nordeste e Sudeste, ou entre mulheres negras e homens brancos, é provavelmente o achado mais relevante que ainda não temos.</div>
</div>
`);

S.push(`
<div class="eyebrow">Perguntas 4 e 5</div>
<h2>Proteção, segurança e o veredito comparativo</h2>
<div class="chartwrap">__ANS_P4__</div>
<div class="body" style="margin-top:1.6vh"><div class="col">
<h3 style="color:var(--warn)">4a. Proteção: sem resposta</h3>
<p>A cobertura de proteção social tem entre 1 e 16 observações por país, e a China tem uma. Fiscalização trabalhista, direitos sindicais e trabalho análogo à escravidão não foram extraídos. <b>Esta pergunta continua aberta e é a maior lacuna do trabalho.</b></p>
</div><div class="col">
<h3>4b. Segurança: melhora clara</h3>
<p>Homicídios caem de 27,2 para 19,3 por 100 mil, redução de 29%, enquanto a mediana latino americana quase dobrou. Ressalva obrigatória: sem a série de mortes por causa indeterminada do DataSUS, parte dessa queda pode ser reclassificação.</p>
</div></div>
<div class="note" style="margin-top:1.4vh"><b>5. O Brasil fez melhor ou pior que os pares?</b> Pior em crescimento, produtividade e investimento. Melhor em distribuição, educação e segurança. Equivalente em pobreza e mortalidade infantil. Não existe um veredito único, e a v3 previu exatamente isso ao separar as perguntas.</div>
`);

S.push(`
<div class="eyebrow">A limitação central</div>
<h2>A série não existe. O que existe são pontos com buracos.</h2>
<p class="mute" style="font-size:.86rem;margin-bottom:1.6vh">Anos com dado <b>observado</b> de Gini e pobreza, 2002 a 2024. Cada célula preenchida é uma pesquisa domiciliar realizada.</p>
__AVAIL__
<div class="legend"><span><b style="background:var(--br)"></b>Brasil</span><span><b style="background:var(--grp)"></b>comparadores</span><span><b style="background:rgba(255,255,255,.09)"></b>sem dado</span></div>
<div class="note" style="margin-top:1.8vh">A Índia tem quatro pontos em 22 anos. A África do Sul tem cinco. <b>A mediana do grupo G20 emergentes para indicadores de distribuição é, na prática, interpolação.</b></div>
`);

S.push(`
<h2>Quatro limitações que quebram a especificação</h2>
<p style="margin-bottom:1.4vh">Não são detalhes de execução. Exigem decisão antes de congelar.</p>
<div class="body"><div class="col">
<ul class="rule">
<li class="w"><b>O buraco de 2020 não existe na base internacional.</b> <span class="mute">A v3 manda não interpolar 2020, porque a PNAD Contínua anual não foi a campo. Mas o World Bank PIP tem pobreza e Gini do Brasil em 2020, derivados de fonte alternativa. A regra e a fonte estão em conflito direto. E <b>2010 está faltando</b>, por ser ano censitário.</span></li>
<li class="w"><b>Cobertura de distribuição assimétrica.</b> <span class="mute">Brasil tem 22 anos observados. Chile tem 10, África do Sul 5, Índia 4.</span></li>
</ul>
</div><div class="col">
<ul class="rule">
<li class="w"><b>As janelas de regime não foram respeitadas.</b> <span class="mute">A janela nominal do boom é 2003 a 2011. Para o Brasil, o cálculo usou 2002 a 2012. Países diferentes usam anos de ponta diferentes dentro da mesma janela. A crítica &ldquo;vocês compararam períodos diferentes&rdquo; procede hoje.</span></li>
<li class="w"><b>Interpolação linear em pesquisa amostral.</b> <span class="mute">Para a Índia, uma reta liga 2011 a 2022. Qualquer reversão real nesse intervalo desapareceu.</span></li>
</ul>
</div></div>
`);

S.push(`
<h2>Indicadores headline sem dado</h2>
<table>
<tr><th>Indicador</th><th>Pergunta</th><th>Situação</th></tr>
<tr><td>Taxa de informalidade</td><td class="mute">1</td><td>Código do World Bank retornou vazio e a API do ILOSTAT não respondeu em duas tentativas. Exige download manual, ou PNAD Contínua com quebra da regra de não mistura.</td></tr>
<tr><td>Renda do bottom 40 (prosperidade compartilhada)</td><td class="mute">2</td><td>O indicador do Banco Mundial é janela móvel calculada em poucos anos de referência, não série anual. Precisa ser reconstruído a partir dos quintis, que estão extraídos.</td></tr>
<tr><td>Insegurança alimentar</td><td class="mute">3</td><td>Só a partir de 2015, com 9 observações. Sem dado para Índia, Turquia e China. Não cobre os três primeiros regimes.</td></tr>
<tr><td>Cobertura de proteção social</td><td class="mute">4a</td><td>Entre 1 e 16 observações por país. China tem 1. Não sustenta comparação por regime.</td></tr>
<tr><td>Dívida do governo sobre PIB</td><td class="mute">transversal</td><td>Ausente para Chile, Argentina, Equador e China. Exige IMF WEO como substituto.</td></tr>
</table>
`);

S.push(`
<h2>O que ainda não foi tocado</h2>
<div class="body"><div class="col stack">
<h3 style="color:var(--grp)">Tier 1 pendente</h3>
<p class="mute">WID.world (participação do 1%, Palma, P90/P10) · UNODC direto · V&#8209;Dem · ITUC Global Rights Index · World Prison Brief · IMF WEO · OMS, excesso de mortalidade para o benchmark de pandemia · Penn World Table</p>
</div><div class="col stack">
<h3 style="color:var(--warn)">Tier 2 pendente, integralmente</h3>
<p class="mute">IBGE e PNAD Contínua · DataSUS e SIM · INEP · SNIS · CadÚnico · BCB · FBSP · Tesouro · Receita Federal · MTE · SISDEPEN</p>
</div></div>
<div class="note" style="margin-top:2.4vh">Consequência prática: <b>não existe nenhuma desagregação por raça, região, gênero ou situação do domicílio nos dados atuais.</b> Numa análise sobre desigualdade brasileira, essa desagregação é frequentemente o próprio achado, e ela está no bloco obrigatório para publicação.</div>
`);

S.push(`
<h2>Cinco decisões antes de seguir</h2>
<div class="body"><div class="col">
<ul class="rule">
<li><b>2020.</b> <span class="mute">Aceitar o valor do PIP declarando a origem, ou remover o ponto e divergir da fonte que a metodologia diz usar.</span></li>
<li><b>Interpolação.</b> <span class="mute">Manter com declaração explícita, ou restringir comparações a anos com dado observado nos dois lados.</span></li>
<li><b>Janelas.</b> <span class="mute">Tolerância zero, ou registrar por país os anos efetivamente usados.</span></li>
</ul>
</div><div class="col">
<ul class="rule">
<li><b>Informalidade.</b> <span class="mute">Download manual do ILOSTAT, ou aceitar PNAD Contínua quebrando a regra de não mistura.</span></li>
<li><b>G20 emergentes em distribuição.</b> <span class="mute">Rebaixar a grupo secundário, ou manter com aviso de cobertura em cada gráfico.</span></li>
</ul>
<p style="margin-top:1.4em">Resolvidas as cinco, o próximo passo é a extração do Tier 2, que é onde está a desagregação e o volume real de trabalho.</p>
</div></div>
`);

S.push(`
<h2>O que a análise não vai fazer</h2>
<div class="body"><div class="col">
<ul class="rule">
<li><b>Atribuir causalidade</b> <span class="mute">a políticas ou governos específicos</span></li>
<li><b>Construir contrafactual</b> <span class="mute">ou controle sintético</span></li>
<li><b>Medir mobilidade intergeracional</b> <span class="mute">como série temporal. O Brasil não tem painel longitudinal cobrindo o período.</span></li>
<li><b>Análise subnacional</b> <span class="mute">por estado ou município</span></li>
<li><b>Projeções</b> <span class="mute">para além de 2026</span></li>
</ul>
</div><div class="col stack">
<p class="lede">Chegar a conclusões diferentes em dimensões diferentes não é falha da análise. É a característica mais importante a preservar.</p>
<p class="mute">O Brasil pode ter melhorado muito e apenas acompanhado a tendência global. Pode ter crescido pouco e distribuído bem. Pode ter crescido bem e concentrado. O resultado pode depender do período, do indicador e do benchmark. Todos esses são resultados legítimos.</p>
</div></div>
`);

S.push(`
<div class="eyebrow">Reprodutibilidade</div>
<h2>Congelar antes de extrair, publicar tudo</h2>
<div class="body"><div class="col">
<ul class="rule">
<li>Matriz de indicadores, composição dos grupos e janelas <b>congeladas e publicadas antes da primeira extração</b></li>
<li>Qualquer alteração posterior registrada em changelog público, com data e justificativa</li>
<li>Toda série publicada com fonte, data de extração e versão da base</li>
</ul>
</div><div class="col">
<ul class="rule">
<li>Código de tratamento e dados brutos publicados junto</li>
<li>Resultados frágeis nos testes de robustez marcados visualmente no material final</li>
<li>Financiamento e vínculos institucionais declarados</li>
</ul>
</div></div>
<p class="mute" style="margin-top:2.6vh;font-size:.82rem">Fonte dos dados apresentados: World Bank API, WDI e PIP. Extração em 06/09/2026, base atualizada em 13/07/2026.</p>
`);

/* ---------- render ---------- */
function availHTML(){
  let h='<div class="avail">';
  h+='<div></div>';
  for(let y=2002;y<=2024;y++) h+='<div style="font-family:IBM Plex Mono;font-size:.55rem;color:#5E7480;text-align:center">'+(y%5===0||y===2002?String(y).slice(2):'')+'</div>';
  h+='<div></div>';
  D.grid.forEach(g=>{
    h+='<div class="nm">'+g.pais+'</div>';
    g.anos.forEach(v=>{h+='<div class="c'+(v?' f':'')+(g.pais==='Brasil'&&v?' br':'')+'"></div>';});
    h+='<div class="tot'+(g.n<12?' low':'')+'">'+g.n+'</div>';
  });
  return h+'</div>';
}

function fmt(v,d,suf){ if(v===null||v===undefined) return 'n/d';
  return (v>0?'+':'')+Number(v).toLocaleString('pt-BR',{minimumFractionDigits:d,maximumFractionDigits:d})+(suf||''); }
function cellDelta(pp,rel,d,inv){
  if(pp===null||pp===undefined) return '<td class="n mute">n/d</td>';
  const bom = inv ? pp>0 : pp<0;
  return '<td class="n '+(bom?'good':'bad')+'">'+fmt(pp,d)+'<span class="mute" style="font-size:.82em"> ('+fmt(rel,0,'%')+')</span></td>';
}
function ansTable(q, inv){
  const rows = D.ans.filter(r=>r.q===q);
  const janelaComum = rows.every(r=>r.anos===rows[0].anos);
  let h='<div style="overflow-x:auto"><table style="min-width:600px"><tr><th>Indicador</th><th style="text-align:right">Brasil, início e fim'
    +(janelaComum?' <span class="mute" style="font-weight:400">('+rows[0].anos.replace('-','–')+')</span>':'')
    +'</th><th style="text-align:right">Δ Brasil</th><th style="text-align:right">Δ América Latina</th><th style="text-align:right">Δ G20 emergentes</th></tr>';
  rows.forEach(r=>{
    const d = (r.unid==='int$')?0:1;
    const up = inv && inv.indexOf(r.ind)>=0;
    const janela = janelaComum ? '' : ' <span class="mute" style="font-size:.82em">('+r.anos.replace('-','–')+')</span>';
    h+='<tr><td>'+r.ind+' <span class="mute" style="font-size:.85em">'+r.unid+'</span></td>'
      +'<td class="n mute">'+Number(r.br_ini).toLocaleString('pt-BR')+' → '+Number(r.br_fim).toLocaleString('pt-BR')+janela+'</td>'
      +cellDelta(r.br_pp,r.br_rel,d,up)+cellDelta(r.lac_pp,r.lac_rel,d,up)+cellDelta(r.g20_pp,r.g20_rel,d,up)+'</tr>';
  });
  return h+'</table></div>';
}
function fomeChart(){
  const bra=D.fome.BRA, lac=D.fome.LAC_MED, g20=D.fome.G20_MED;
  return chart([ser(bra,'#E8A33D','',2.8), ser(lac,'#6FA8A0','',1.8), ser(g20,'#54707E','',1.8,1)],{h:300,step:2,y0:0,alt:'inseguranca alimentar'});
}
/* série de 3, mesma base em toda a apresentação: Brasil, América Latina, G20 sem China */
function ser3(node){
  return [ser(node.bra,'#E8A33D','Brasil',2.6),
          ser(node.lac,'#6FA8A0','Am. Latina',1.8),
          ser(node.g20,'#54707E','G20 s/ China',1.8,1)];
}
const CH = {
 CH_POV: chart(ser3(D.pov),{h:360,bands:BANDS,y0:0,mr:34,alt:'pobreza extrema'}),
 CH_GINI: chart(ser3(D.gini),{h:300,step:6,mr:34,alt:'gini'}),
 CH_B40: chart(ser3(D.b40),{h:300,step:6,mr:34,alt:'bottom 40'}),
 CH_PIB: chart(ser3(D.idx.pib),{h:300,bands:BANDS,mr:34,alt:'pib per capita indexado'}),
 CH_PROD: chart(ser3(D.idx.prod),{h:300,bands:BANDS,mr:34,alt:'produtividade indexada'}),
 CH_IMR: chart(ser3(D.imr),{h:270,step:6,y0:0,ticks:3,mr:30,alt:'mortalidade'}),
 CH_SAN: chart(ser3(D.san),{h:270,step:6,ticks:3,mr:30,alt:'saneamento'}),
 CH_HOM: chart(ser3(D.hom),{h:270,step:6,y0:0,ticks:3,mr:30,alt:'homicidios'}),
 CH_DES: chart(ser3(D.des),{h:270,step:6,y0:0,ticks:3,mr:30,alt:'desemprego'}),
};

const deck=document.getElementById('deck');
S.forEach((html,i)=>{
  let h=html.replace('__ANS_P1__',ansTable('P1',['Investimento sobre PIB']))
             .replace('__ANS_P2__',ansTable('P2',['Participação dos 40% mais pobres']))
             .replace('__ANS_P3__',ansTable('P3',['Saneamento básico','Ensino médio completo (25+)']))
             .replace('__ANS_P4__',ansTable('P4b',[]))
             .replace('__CH_FOME__',fomeChart())
             .replace('__AVAIL__',availHTML());
  Object.keys(CH).forEach(k=>{h=h.replace('__'+k+'__',CH[k]);});
  const d=document.createElement('section');
  d.className='slide'; d.innerHTML=h; d.setAttribute('aria-hidden','true');
  deck.appendChild(d);
});
const slides=[...document.querySelectorAll('.slide')];
let cur=0;
function show(i){
  cur=Math.max(0,Math.min(slides.length-1,i));
  slides.forEach((s,j)=>{s.classList.toggle('on',j===cur); s.setAttribute('aria-hidden',j!==cur);});
  document.getElementById('bar').style.width=((cur+1)/slides.length*100)+'%';
  document.getElementById('cnt').textContent=String(cur+1).padStart(2,'0')+' / '+slides.length;
  slides[cur].scrollTop=0;
}
addEventListener('keydown',e=>{
  if(['ArrowRight','ArrowDown',' ','PageDown'].includes(e.key)){e.preventDefault();show(cur+1);}
  if(['ArrowLeft','ArrowUp','PageUp'].includes(e.key)){e.preventDefault();show(cur-1);}
  if(e.key==='Home')show(0); if(e.key==='End')show(slides.length-1);
});
addEventListener('click',e=>{
  if(e.target.closest('a'))return;
  show(e.clientX < innerWidth*0.28 ? cur-1 : cur+1);
});
show(0);
</script>
</body>
</html>"""

os.makedirs(DOCS, exist_ok=True)
destino = os.path.join(DOCS, 'apresentacao.html')
open(destino, 'w').write(HTML.replace('__DATA__', json.dumps(D)))
print('apresentacao escrita em', destino)
