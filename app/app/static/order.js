
function load(){
    const days_input = document.querySelector('input[name=days]')
    const total_price = document.querySelector('#total_price')
    days_input.addEventListener('input', () => {
        if(days_input.value){
            total_price.innerHTML = `Cena za ${days_input.value} dni: ${days_input.value * price_per_day}zł`
        }
        else{
            total_price.innerHTML = ''
        }
    })
}

window.addEventListener('load', load)
