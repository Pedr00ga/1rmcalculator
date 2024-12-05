function calcula1RM(carga, reps, rpe) {
    let rir = 10 - rpe;
    let coef = 0.03;
    let primeiro = (36 / (37 - reps));
    let segundo = carga * primeiro;
    let terceiro = rir * coef;
    let quarto = 1 - terceiro;
    let rmestimado = (segundo + 6) / quarto;

    return rmestimado.toFixed(2);
  }

  document.getElementById('rm-form').addEventListener('submit', function(event) {
    event.preventDefault();

    const carga = parseFloat(document.getElementById('carga').value);
    const reps = parseFloat(document.getElementById('reps').value);
    const rpe = parseFloat(document.getElementById('rpe').value);

    if (isNaN(carga) || isNaN(reps) || isNaN(rpe) || carga <= 0 || reps <= 0 || rpe <= 0) {
        document.getElementById('onerepmax').innerText = 'Por favor, insira valores válidos.';
        return;
    }

    const onerepmax = calcula1RM(carga, reps, rpe);
    document.getElementById('onerepmax').innerText = `${onerepmax} kg`;
  });