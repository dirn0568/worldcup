var picture_array = new Array();
picture_array[0] = "../static/bg01.png";
picture_array[1] = "../static/bg02.png";
picture_array[2] = "../static/bg03.png";
picture_array[3] = "../static/bg04.png";

const playground = document.querySelector(".playground");
var randomIndex = Math.floor(Math.random() * picture_array.length)
var randomIndex2 = Math.floor(Math.random() * picture_array.length)
var Indexlistget = new Array();
var Indexlistpop = new Array();




Indexcheck();
playImage();
console.log(randomIndex, randomIndex2)



function Indexcheck(){
    while (randomIndex==randomIndex2) {
        randomIndex2 = Math.floor(Math.random() * picture_array.length);
        console.log('진행중1')
    }
}
function Playgame(){
    console.log(Indexlistget)
    console.log(Indexlistpop)
    while (randomIndex==randomIndex2 || Indexlistget.includes(randomIndex) || Indexlistpop.includes(randomIndex) || Indexlistget.includes(randomIndex2) || Indexlistpop.includes(randomIndex2)) {
        randomIndex = Math.floor(Math.random() * picture_array.length)
        randomIndex2 = Math.floor(Math.random() * picture_array.length)
        console.log('진행중2')
    }
    console.log(randomIndex, randomIndex2)
}

function Playcheck(num, num2){
    Indexlistget.push(num)
    Indexlistpop.push(num2)
    Playgame()
    playImage()
}
//playground.prepend(document.createElement("ul"))
//const ul = document.createElement("img")
//playground.prepend(ul)
//const ull = document.createElement("src=picture_array[0]")
//playground.append(ull)
function playImage(){
    var output = '<button ';
    output += 'onclick="Playcheck(randomIndex, randomIndex2)">';
    output += '<img src=';
    output += picture_array[randomIndex];
    output += '>';
    output += '</button>';
    output += '<button ';
    output += 'onclick="Playcheck(randomIndex2, randomIndex)">';
    output += '<img src=';
    output += picture_array[randomIndex2];
    output += '>';
    output += '</button>';
    document.body.innerHTML = output;
    //playground.prepend(output)
}




