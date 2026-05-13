const audio = document.getElementById('audio');
const barra = document.getElementById('barra-progresso');
const barraVolume = document.getElementById('barra-volume');
const tempoAtual = document.getElementById('tempo-atual');
const tempoTotal = document.getElementById('tempo-total');
const canvas = document.getElementById('canvas-ondas');
const ctx = canvas.getContext('2d');
let animando = false;

function formatarTempo(segundos) {
    const min = Math.floor(segundos / 60);
    const seg = Math.floor(segundos % 60);
    return `${min}:${seg.toString().padStart(2, '0')}`;
}

function buscar() {
    let humor = document.getElementById('humor').value;
    if (!humor) return;

    let gostos = [
        document.getElementById('t1').value,
        document.getElementById('t2').value,
        document.getElementById('t3').value
    ].filter(m => m !== '');

    document.getElementById('header').style.display = 'none';
    document.getElementById('loading').style.display = 'flex';
    document.getElementById('resultado').style.display = 'none';

    fetch('/buscar', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ humor: humor, gostos: gostos })
    })
    .then(res => res.json())
    .then(data => {
        document.getElementById('loading').style.display = 'none';
        document.getElementById('resultado').style.display = 'flex';

        document.getElementById('capa').src = data.capa;
        let partes = data.nome.split(' - ');
        document.getElementById('artista').textContent = partes[0] || '';
        document.getElementById('nome').textContent = partes[1] || data.nome;
        audio.src = data.preview;
        audio.volume = barraVolume.value;
        document.getElementById('play').innerText = '▶';

        redimensionarCanvas();
    });
}

function togglePlay() {
    const botao = document.getElementById('play');
    if (audio.paused) {
        audio.play();
        botao.innerText = '⏸';
        if (!animando) desenharOndas();
    } else {
        audio.pause();
        botao.innerText = '▶';
        animando = false;
    }
}

audio.addEventListener('loadedmetadata', () => {
    barra.max = audio.duration;
    tempoTotal.textContent = formatarTempo(audio.duration);
});

audio.addEventListener('timeupdate', () => {
    barra.value = audio.currentTime;
    tempoAtual.textContent = formatarTempo(audio.currentTime);
});

audio.addEventListener('ended', () => {
    document.getElementById('play').innerText = '▶';
    animando = false;
    ctx.clearRect(0, 0, canvas.width, canvas.height);
});

barra.addEventListener('input', () => {
    audio.currentTime = barra.value;
});

barraVolume.addEventListener('input', () => {
    audio.volume = barraVolume.value;
});

function redimensionarCanvas() {
    canvas.width = window.innerWidth;
    canvas.height = window.innerHeight;
}

// function desenharOndas() {
//     animando = true;
//     const barras = 60;
//     const larguraBarra = canvas.width / barras;

//     function frame() {
//         if (!animando) return;
//         ctx.clearRect(0, 0, canvas.width, canvas.height);

//         for (let i = 0; i < barras; i++) {
//             const altura = 20 + Math.random() * (canvas.height * 0.6);
//             const x = i * larguraBarra;
//             const y = (canvas.height - altura) / 2;
//             ctx.fillStyle = 'rgba(26, 58, 107, 0.25)';
//             ctx.beginPath();
//             ctx.roundRect(x + 2, y, larguraBarra - 4, altura, 4);
//             ctx.fill();
//         }
//         requestAnimationFrame(frame);
//     }
//     frame();
// }

window.addEventListener('resize', redimensionarCanvas);