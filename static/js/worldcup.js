var picture_array = new Array();
picture_array[0] = "/static/001.webm";
picture_array[1] = "/static/002.webm";
picture_array[2] = "/static/003.webm";
picture_array[3] = "/static/004.webm";
picture_array[4] = "/static/005.mp4";
picture_array[5] = "/static/006.mp4";
picture_array[6] = "/static/007.mp4";
picture_array[7] = "/static/008.mp4";


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
    video1.load();
    video2.load();
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
    console.log(picture_array, '#!$%!%!@#$%!#%!#@%!@#이거지롱')
    console.log(picture_array[0], '#!$%!%!@#$%!#%!#@%!@#이거지롱')
//    console.log(picture_array[0] -= '/static')
    Indexlistget.splice(0);
    Indexlistpop.splice(0);
}

function EndGame(){
    console.log('이거는 작동할테고')
    if (picture_array.length % 2 == 1){
        console.log('이거는 작동하냐')
//        localStorage.setitem('keyyy', 'vallllue')
        console.log(picture_array)
        console.log(picture_array[0])
        window.location.replace("//158.247.198.187//play/worldcup_test" + picture_array[0]);
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
    play_div.setAttribute('style', 'float: left; width: 40%');
    play_box = document.createElement('a');
    play_box.setAttribute('href', '#');
    play_box.onclick=function(){Playcheck(randomIndex, randomIndex2)};
    play_img = document.createElement('video');
    play_img.setAttribute('id', 'video1');
    play_img.setAttribute('controls', 'mute');
    play_img.setAttribute('width', '100%;');
    play_img.setAttribute('height', '100%;');
    console.log(picture_array[randomIndex]);
    play_img.setAttribute('src', picture_array[randomIndex]);

    document.body.append(play_div);
    play_div.append(play_box);
    play_box.append(play_img)


    play_div2 = document.createElement('div');
    play_div2.setAttribute('style', 'padding: 10rem 5rem 0px 7rem; float: left;');
    play_vs = document.createElement('h1');
    play_div2.append('VS');
    document.body.append(play_vs);
    play_vs.append(play_div2);

    play_div3 = document.createElement('div');
    play_div3.setAttribute('style', 'float: right; width: 40%;');
    play_box2 = document.createElement('a');
    play_box2.setAttribute('href', '#');
    play_box2.setAttribute('video', 'pause');
    play_box2.onclick=function(){Playcheck(randomIndex2, randomIndex)};
    play_img2 = document.createElement('video');
    play_img2.setAttribute('id', 'video2');
    play_img2.setAttribute('controls', 'mute');
    play_img2.setAttribute('width', '100%;');
    play_img2.setAttribute('height', '100%;');
    play_img2.setAttribute('src', picture_array[randomIndex2]);
    document.body.append(play_div3);
    play_div3.append(play_box2);
    play_box2.append(play_img2);
}



