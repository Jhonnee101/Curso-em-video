function carregar () {
    var msg = window.document.getElementById('msg')
    var img = window.document.getElementById('imagem')
    var data = new Date()
    var hora = data.getHours()
    msg.innerHTML = `Agora sao ${hora} Horas`
    if (hora >= 0 && hora <12){
        //Bom dia
        img.src = 'fotomanha.png'
        document.body.style.background = '#e2cd9f'
    }else if(hora >= 12 && hora <18){
        //Boa tarde
        img.src = 'fototarde.png'
        document.body.style.background = '#A0522D'
    }else {
        //Boa noite
        img.src = 'fotonoite.png'
        document.body.style.background = '#4B0082'
    }
}