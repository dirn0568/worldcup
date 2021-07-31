import BLOCKS from "./blocks.js"

//DOM
const playground = document.querySelector(".playground > ul");
const gameText = document.querySelector(".game-text");
const scoreDisplay = document.querySelector(".score");
const restartButton = document.querySelector(".game-text > button");
// Setting
const GAME_ROWS = 20;
const GAME_COLS = 10;

// variables
let score = 0;
let duration = 500;
let downInterval;
let tempMovingItem;

const movingItem = {
    type: "",
    direction: 0,
    top: 4,
    left: 3,
};


init()
console.log(playground)

// functions
// { ...movingItem } 이해가 잘안됨 내일 다시한번 봐볼껏
function init(){
    tempMovingItem = { ...movingItem };

    for (let i = 0; i < GAME_ROWS; i++) {
        prependNewLine()
    }
    generateNewBlock()
}

function prependNewLine() {
    const li = document.createElement("li");
    const ul = document.createElement("ul");
    for (let j=0; j<GAME_COLS; j++){
        const matrix = document.createElement("li");
        ul.prepend(matrix);
    }
    li.prepend(ul)
    playground.prepend(li)
}

// const { type, direction, top, left } = tempMovingItem; tempMovingItem의 데이터가 알아서 저 리스트 안에 들어가는게 가능?
// 삼학연산자 내일 다시보기(삼학연산자가 없어도 아마될꺼 같음 왜냐하면 없어도 None타입 데이터가 나오기때문에)
// html 에서 <ul> enter </ul> 이런식으로 저장되면 enter부분을 text로 인식되어서 top으로 내릴때 두번내려야했던거임 <ul></ul> 이렇게 바로 저장해야함
// 유튜브 1시간 10분 17초까지의 상황
function renderBlocks(moveType="") {
    const { type, direction, top, left } = tempMovingItem;
    const movingBlocks = document.querySelectorAll(".moving");
    movingBlocks.forEach(moving => {
        moving.classList.remove(type, "moving");
    })
    BLOCKS[type][direction].some(block => {
        const x = block[0] + left;
        const y = block[1] + top;
        const target = playground.childNodes[y] ? playground.childNodes[y].childNodes[0].childNodes[x] : null;
        const isAvailable = checkEmpty(target);
        if (isAvailable) {
            target.classList.add(type, "moving")
        } else {
            tempMovingItem = { ...movingItem }
            if(moveType === 'retry'){
                clearInterval(downInterval)
                showGameoverText()
            }
            setTimeout(() => {
                renderBlocks('retry');
                if (moveType === "top") {
                    seizeBlock();
                }
            }, 0)
            return true;
        }
    })
//    console.log('play', "################################")
    movingItem.left = left;
    movingItem.top = top;
    movingItem.direction = direction;
}
function checkEmpty(target){
    if(!target || target.classList.contains("seized")){
        return false;
    }
    return true;
}

function seizeBlock(){
    const movingBlocks = document.querySelectorAll(".moving");
    movingBlocks.forEach(moving => {
        moving.classList.remove("moving");
        moving.classList.add("seized");
    })
    checkMatch()
}

function checkMatch(){
    const childNodes = playground.childNodes;
    childNodes.forEach(child => {
        let matched = true;
        child.children[0].childNodes.forEach(li => {
            if(!li.classList.contains("seized")){
                matched = false;
            }
        })
        if(matched){
            child.remove();
            prependNewLine()
            score += 100;
            console.log(score)
            scoreDisplay.innerText = score;
            if (score % 500 == 0){
                duration -= 50;
            }
        }
    })
    generateNewBlock()
}

function generateNewBlock(){

    clearInterval(downInterval);
    downInterval = setInterval(()=>{
        moveBlock('top', 1)
    }, duration)

    const blockArray = Object.entries(BLOCKS);
    const randomIndex = Math.floor(Math.random() * blockArray.length)

    movingItem.type = blockArray[randomIndex][0]
    movingItem.top = 0;
    movingItem.left = 3;
    movingItem.direction = 0;
    tempMovingItem = { ...movingItem };
    renderBlocks()
}

function moveBlock(moveType, amount){
    tempMovingItem[moveType] += amount
    renderBlocks(moveType)
}

function changeDirection(){
    const direction = tempMovingItem.direction;
    direction === 3 ? tempMovingItem.direction = 0 : tempMovingItem.direction += 1;
    renderBlocks()
}

function dropBlock(){
    clearInterval(downInterval);
    downInterval = setInterval(() => {
        moveBlock("top", 1)
    }, 10)
}

function showGameoverText(){
    gameText.style.display = "flex"
}

// event handling
document.addEventListener("keydown", e => {
    switch(e.keyCode){
        case 39:
            moveBlock("left", 1);
            break;
        case 37:
            moveBlock("left", -1)
            break;
        case 40:
            moveBlock("top", 1);
            break;
        case 32:
            changeDirection();
            break;
        case 38:
            dropBlock();
            break;
        default:
            break;
    }
})

//function test() {
//    console.log(setInterval( "alert('good')", 1000))
//}
