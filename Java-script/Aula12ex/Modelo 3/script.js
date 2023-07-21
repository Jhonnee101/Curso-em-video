function verificar(){
    var data = new Date()
    var ano = data.getFullYear()
    var fano = document.getElementById('txtano')
    var res = document.getElementById('res')

    if (fano.value.length == 0 || fano.value > ano){
        window.alert('Verifique os dados e tente novamente')
    } else {
        var fsex = document.getElementsByName('radsex')
        var idade = ano - Number(fano.value)
        var genero = ''
        var img = document.createElement('img')
        img.setAttribute('id','foto')
        if (fsex[0].checked){
            genero = 'Homem'
            if (idade >= 0 && idade < 10 ){
                //Crianca
                img.setAttribute('src', 'criancam.jpg')
            }else if (idade < 21){
                //Jovem
                img.setAttribute('src', 'jovem m.jpg')
            }else if (idade < 50 ){
                 //Adulto
                 img.setAttribute('src', 'adultom.jpg')
            }else{
                //Idoso
                img.setAttribute('src', 'idosom.jpg')
            }
            } else if (fsex[1].checked) {
            genero = 'Mulher'
            if (idade >= 0 && idade < 10 ){
                //Crianca
                img.setAttribute('src', 'criancaf.jpg')
            }else if (idade < 21){
                //Jovem
                img.setAttribute('src', 'jovemf.jpg')
            }else if (idade < 50 ){
                 //Adulto
                 img.setAttribute('src', 'adultof.jpg')
            }else{
                //Idoso
                img.setAttribute('src', 'idosof.jpg')
            }
        }
        res.innerHTML = `Detectamos o genero ${genero} com ${idade}`
        res.appendChild(img)

    }
}