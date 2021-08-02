var picture_array = new Array();
picture_array[0] = "../static/bg01.png";
picture_array[1] = "../static/bg02.png";
picture_array[2] = "../static/bg03.png";
picture_array[3] = "../static/bg04.png";
picture_array[4] = "../static/bg05.png";
picture_array[5] = "../static/bg06.png";
picture_array[6] = "../static/bg07.png";
picture_array[7] = "../static/bg08.png";


var randomIndex = 0
var randomIndex2 = 0
var Indexlistget = new Array();
var Indexlistpop = new Array();
var end = false;
var stage = 8;
var stage2 = stage / 2;
var round = 1;

let play_img;
let play_img2;
let play_box;
let play_box2;



Init();
Indexcheck();
playImage();

function Init(){
    randomIndex = Math.floor(Math.random() * picture_array.length)
    randomIndex2 = Math.floor(Math.random() * picture_array.length)
}

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
        if (picture_array.length % 2 == 1){
            break;
        }
        randomIndex = Math.floor(Math.random() * picture_array.length)
        randomIndex2 = Math.floor(Math.random() * picture_array.length)
        console.log('진행중2')
    }
    console.log(randomIndex, randomIndex2)
}

function Playcheck(num, num2){
    Indexlistget.push(num)
    Indexlistpop.push(num2)
    round++;
    if (picture_array.length == Indexlistget.length + Indexlistpop.length){
        Nextlevel()
        EndGame()
        Init()
        stage = stage / 2;
        stage2 = stage2 / 2;
        round = 1
    }
    Playgame()
    playImage()
    if (end){
        EndGame()
    }
}

function Nextlevel(){
    var i = 0;
    while (i < Indexlistget.length)  {
        console.log('여기서 멈추나')
        picture_array.push(picture_array[Indexlistget[i]])
        i++;
    }
    console.log(picture_array)
    picture_array.splice(0, Indexlistget.length*2);
    console.log(picture_array)
    Indexlistget.splice(0);
    Indexlistpop.splice(0);
}

function EndGame(){
    console.log('이거는 작동할테고')
    if (picture_array.length % 2 == 1){
        console.log('이거는 작동하냐')
//        localStorage.setitem('keyyy', 'vallllue')
        window.location.replace("//127.0.0.1:8000/play/worldcup_create");
//        url.searchParams.set('data', data);
        document.body.innerHTML = ''
        play_img = document.createElement('img');
        play_img.setAttribute('style', 'width: 50rem; height: 50rem;');
        play_img.setAttribute('src', picture_array[0]);
        document.body.append(play_img);
        console.log('끝났습니다.')
        end = true;
    }
}



function playImage(){
    document.body.innerHTML = ''
    play_time = document.createElement('h1');
    play_time.setAttribute('style', 'text-align: center;');
    play_time.append(stage);
    play_time.append('강 ');
    play_time.append(stage2);
    play_time.append('/');
    play_time.append(round);
    document.body.append(play_time);

    play_div = document.createElement('div');
    play_div.setAttribute('style', 'float: left;');
    play_box = document.createElement('a');
    play_box.setAttribute('href', '#none');
    play_box.onclick=function(){Playcheck(randomIndex, randomIndex2)};
    play_img = document.createElement('img');
    play_img.setAttribute('style', 'width: 50rem; height: 50rem;');
    play_img.setAttribute('src', picture_array[randomIndex]);

    document.body.append(play_box);
    play_box.append(play_div);
    play_div.append(play_img)


    play_div2 = document.createElement('div');
    play_div2.setAttribute('style', 'padding: 10rem 5rem 0px 5rem; float: left;');
    play_vs = document.createElement('h1');
    play_div2.append('VS');
    document.body.append(play_vs);
    play_vs.append(play_div2);

    play_div3 = document.createElement('div');
    play_div3.setAttribute('style', 'float: left;');
    play_box2 = document.createElement('a');
    play_box2.setAttribute('href', '#none');
    play_box2.onclick=function(){Playcheck(randomIndex2, randomIndex)};
    play_img2 = document.createElement('img');
    play_img2.setAttribute('style', 'width: 50rem; height: 50rem;');
    play_img2.setAttribute('src', picture_array[randomIndex2]);
    document.body.append(play_div3);
    play_div3.append(play_box2);
    play_box2.append(play_img2);
}



