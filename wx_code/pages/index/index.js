var app = getApp()
Page({
  data: {
    output: '',
    pro: {},
    textHead: '',
    showviewSu: false,
    showviewfail: false,
    showview404: false,
    showmain:true,
    images: {}
  },
  imageLoad: function (e) {
    var $width = e.detail.width,    //获取图片真实宽度
      $height = e.detail.height,
      ratio = $width / $height;    //图片的真实宽高比例
    var viewWidth = 718,           //设置图片显示宽度，左右留有16rpx边距
      viewHeight = 718 / ratio;    //计算的高度值
    var image = this.data.images;
    //将图片的datadata-index作为image对象的key,然后存储图片的宽高值
    image[e.target.dataset.index] = {
      width: viewWidth,
      height: viewHeight
    }
    this.setData({
      images: image
    })
  },
  onLoad: function () {
    var that = this;
    that.setData({
      output: '快点击下面的按钮扫一扫吧！',
    })
  },
  scanner: function () {
    var that = this;
    wx.scanCode({
      success: (res) => {
        var urls = 'https://stringair.xin/api-taozi/wechat/product_check_code=' + res.result
        wx.request({
          url: urls,
          method: 'GET',
          data: {},
          header: {
            'Accept': 'application/json',
            'Authorization': 'Basic V2VjaGF0Z2V0aW5mbzpFaVNKUFJTTG93SzY='
          },
          success: function (res) {
            console.log(res.data.data)
            console.log(res.data.status)
            if (res.data.status == 200) {
              wx.showToast({
                title: '成功检测',
                icon: 'success',
                duration: 2000
              })
              res.data.data[0].creatTime = res.data.data[0].creatTime.substring(0, 10)
              res.data.data[0].updateTime = res.data.data[0].updateTime.substring(0, 10)
              that.setData({
                textHead: '这是正品奥,恭喜！',
                output: '点击底部按钮继续扫码',
                pro: res.data.data[0],
                showviewSu: true,
                showmain:false,
                showview404:false,
                showviewfail:false
              })
            } else if (res.data.status == 404) {
              wx.showToast({
                title: '产品未注册',
                icon: 'loading',
                duration: 1000
              })
              that.setData({
                textHead: '抱歉。该商品的未注册或者注册信息已过期',
                output: '点击底部按钮继续扫码',
                showviewSu: false,
                showmain: false,
                showview404: true,
                showviewfail: false
              })
            } else if (res.data.status == 500) {
              wx.showToast({
                title: '未知的二维码',
                icon: 'loading',
                duration: 1000
              })
              that.setData({
                textHead: '我们仅支持在Stringair平台注册的商品，其他未知二维码无法进行验证',
                output: '点击底部按钮继续扫码',
                showviewSu: false,
                showmain: false,
                showview404: false,
                showviewfail: true
              })
            }
          }
        })
      },
    })
  }
})