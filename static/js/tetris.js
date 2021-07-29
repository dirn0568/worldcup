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
        [],
        [],
        [],
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
// 삼학연산자 내일 다시보기
// 유튜브 39분 47초까지의 상황
function renderBlocks() {
    const { type, direction, top, left } = tempMovingItem;
    const movingBlocks = document.querySelectorAll(".moving");
    movingBlocks.forEach(moving => {
        moving.classList.remove(type, "moving");
    })
    BLOCKS[type][direction].forEach(block => {
        const x = block[0] + left;
        const y = block[1] + top;
        const target = playground.childNodes[y] ? playground.childNodes[y].childNodes[0].childNodes[x] : null;
        console.log(target, '@@@@@@@@@@@@@@')
        const isAvailable = checkEmpty(target);
        if (isAvailable) {
            target.classList.add(type, "moving")
        } else {
//            console.log('stop')
            tempMovingItem = { ...movingItem }
            setTimeout(() => {
                renderBlocks();
            }, 0)

        }
    })
    movingItem.left = left;
    movingItem.top = top;
    movingItem.direction = direction;
}
function checkEmpty(target){
    if(!target){
        return false;
    }
    return true;
}


function moveBlock(moveType, amount){
    tempMovingItem[moveType] += amount
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
        default:
            break;
    }
})