window.requestAnimationFrame = function () {
    // 检查浏览器是否支持requestAnimationFrame函数
    return (
        window.requestAnimationFrame ||
        window.webkitRequestAnimationFrame ||
        window.mozRequestAnimationFrame ||
        window.oRequestAnimationFrame ||
        window.msRequestAnimationFrame ||
        // 如果这些选项都不可用，使用设置超时来调用回调函数
        function (callback) {
            window.setTimeout(callback)
        }
    )
}

//初始化函数
function init(elemid) {
// 获取canvas元素
    let canvas = document.getElementById(elemid)
//     获取2d绘图上下文
    c = canvas.getContext('2d')
//     设置canvas的宽度为窗口内宽度，高度为窗口内高度
    w = (canvas.width = window.innerWidth)
    h = (canvas.height = window.innerHeight)
//     设置填充样式为半透明黑
    c.fillStyle = "rgba(30,30,30,1)"
//     使用填充样式填充整个canvas
    c.fillRect(0, 0, w, h)
//     返回绘图上下文和canvas元素
    return {c: c, canvas: canvas}
}

//等待页面加载完成后执行函数
window.onload = function () {
// 获取绘图上下文和canvas元素
    let c = init("canvas").c,
        canvas = init("canvas").canvas,
//         设置canvas的宽度为窗口内宽度，高度为窗口内高度
        w = (canvas.width = window.innerWidth),
        h = (canvas.window = window.innerHeight),
//         初始化鼠标对象
        mouse = {x: false, y: false},
        last_mouse = {}

//     定义计算两点距离的函数
    function dist(p1x, p1y, p2x, p2y) {
        return Math.sqrt(Math.pow(p2x - p1x, 2) + Math.pow(p2y - p1y, 2))
    }

// 定义segment类
    class segment {


        //     构造函数，用于初始化segment对象
        constructor(parent, l, a, first) {
            //     如果是第一条触手段，则位置坐标为触手顶部位置
            //     否则位置坐标为上一个segment对象的nextPos坐标
            this.first = first
            if (first) {
                this.pos = {
                    x: parent.x,
                    y: parent.y,
                }
            } else {
                this.pos =
                    {
                        x: parent.nextPos.x,
                        y: parent.nextPos.y,
                    }
            }
            //     设置segment的长度和角度
            this.L = l
            this.ang = a
            //     计算下一个segment的坐标位置
            this.nextPos = {
                x: this.pos.x + this.L * Math.cos(this.ang),
                y: this.pos.y + this.L * Math.sin(this.ang),
            }
        }

        //     更新segment位置的方法
        update(t) {
            //     计算segment与目标点的角度
            this.ang = Math.atan2(t.y - this.pos.y, t.x - this.pos.x)
            //     根据目标点和角度更新位置坐标
            this.pos.x = t.x + this.L * Math.cos(this.ang - Math.PI)
            this.pos.y = t.y + this.L * Math.sin(this.ang - Math.PI)
            //     根据新的位置坐标更新nextPos坐标
            this.nextPos.x = this.pos.x + this.L * Math.cos(this.ang)
            this.nextPos.y = this.pos.y + this.L * Math.sin(this.ang)
        }

        //     将segment回执为初始位置的方法
        fallback(t) {
            //     将位置坐标设置为目标点坐标
            this.pos.x = t.x
            this.pos.y = t.y
            this.nextPos.x = this.pos.x + this.L * Math.cos(this.ang)
            this.nextPos.y = this.pos.y + this.L * Math.sin(this.ang)
        }

        show() {
            c.lineTo(this.nextPos.x, this.nextPos.y)
        }
    }
    
}