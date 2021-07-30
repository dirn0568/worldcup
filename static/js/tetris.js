//DOM
const playground = document.querySelector(".playground > ul");

// Setting
const GAME_ROWS = 20;
const GAME_COLS = 10;

// variables
let score = 0;
let duration = 500;
let downInterval;
let tempMovingItem;

const BLOCKS = {
    tree: [
        [[2, 1], [0, 1], [1, 0], [1, 1]],
        [[1, 2], [0, 1], [1, 0], [1, 1]],
        [[1, 2], [0, 1], [2, 1], [1, 1]],
        [[2, 1], [1, 2], [1, 0], [1, 1]],
    ]
}

const movingItem = {
    type: "tree",
    direction: 0,
    top: 4,
    left: 3,
};


init()

// functions
// { ...movingItem } 이해가 잘안됨 내일 다시한번 봐볼껏
function init(){
    tempMovingItem = { ...movingItem };

    for (let i = 0; i < GAME_ROWS; i++) {
    prependNewLine()
    }
    renderBlocks()
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
// 유튜브 50분 40초까지의 상황
function renderBlocks(moveType="") {
    const { type, direction, top, left } = tempMovingItem;
    const movingBlocks = document.querySelectorAll(".moving");
    movingBlocks.forEach(moving => {
        moving.classList.remove(type, "moving");
    })
    BLOCKS[type][direction].some(block => {
        const x = block[0] + left;
        const y = block[1] + top;
//        console.log(playground.childNodes[y])
        const target = playground.childNodes[y] ? playground.childNodes[y].childNodes[0].childNodes[x] : null;
        console.log(target)
        const isAvailable = checkEmpty(target);
        if (isAvailable) {
            target.classList.add(type, "moving")
        } else {
            console.log('stop')
            tempMovingItem = { ...movingItem }
            setTimeout(() => {
//                console.log('stop', "####################")
                renderBlocks();
//                console.log('stop2', "####################")
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
    generateNewBlock()
}

function generateNewBlock(){
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
        default:
            break;
    }
})