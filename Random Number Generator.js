function roll_the_dice() {
    let number_of_dice = document.getElementById('number_of_dice').value;
    let type_of_dice = document.getElementById('type_of_dice').value;
    let output_container = document.getElementById('output_container');

    output_container.innerHTML = "";

    if (Number.isInteger(Number(number_of_dice)) && number_of_dice > 0 && type_of_dice) {
        let results = [];
        let dice_output_container = "";

        for (let i = 0; i < number_of_dice; i++) {
            let rollResult = Math.floor(Math.random() * type_of_dice) + 1;
            results.push(rollResult);
        }

        results.forEach(result => {
            dice_output_container += `<div class="dice_output_container">${result}</div>`;
        });         

        output_container.innerHTML = dice_output_container;
    }
    else {
        output_container.innerHTML = "Please enter a valid number of dice (an integer greater than 0) and select a dice type.";
    }
}

