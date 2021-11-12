class ValidarRut {
    constructor(rut) {
        this.rut = rut;
        this.dv = rut.substring(rut.length - 1);
        this.rut = this.rut.substring(0, this.rut.length - 1).replace(/\D/g, '');       
        this.validado = this.validacionRut();
    }

    validacionRut() {
        let numerosArray = this.rut.split('').reverse()
        let contador = 0;
        let multiplicador = 2;

        for (let numero of numerosArray) {
            contador += parseInt(numero) * multiplicador;
            multiplicador++;

            if (multiplicador == 8) {
                multiplicador = 2;
            }
        }

        let dv = 11 - (contador % 11);

        if (dv == 11)
            dv = '0'
        
        if (dv == 10)
            dv = 'k';
  
        return dv == this.dv.toLowerCase();
    }

    formato() {
        if (!this.validado) return '';

        return (this.rut.toString().replace(/\B(?=(\d{3})+(?!\d))/g, '.')) + '-' + this.dv;
    }
}