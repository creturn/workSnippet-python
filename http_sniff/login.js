<!DOCTYPE html>
<html>
<head>
<meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
<title>百度帐号登录</title>
<link type="text/css" rel="stylesheet" href="/style/v3/reset.css?cdnversion=20130110" />
<link type="text/css" rel="stylesheet" href="/style/v3/global.css?cdnversion=20130110" />
<link type="text/css" rel="stylesheet" href="/style/v3/v3_page_login.css?cdnversion=20130110" />
<script type="text/javascript" src="/js/tangram-2.0.js?cdnversion=20130110"></script>
<script type="text/javascript" src="https://passport.baidu.com/passApi/js/wrapper.js?cdnversion=20130110"></script>
</head>
<body>
<div id="wrapper" class="grid-95">
    <div id="header">
        <a href="http://www.baidu.com" class="logo"><img alt="baidu" src="/img/logo.gif"></a>
    </div>
    
    <div id="content" class="clearfix">
        <div class="passPro grid-69 left">
            <div><img src="/img/v2/bigeye.png" alt=""/></div>
            <ul>
                <li class="m-list clearfix zhidao">
                    <span><img src="/img/v2/icon1.png" alt=""/></span>
                    <h4>知道</h4>
                    <p>百度知道是由全球最大的中文搜索引擎百度自主研发、基于搜索的互动式知识问答分享平台。</p>
                </li>
                <li class="m-list clearfix space">
                    <span><img src="/img/v2/icon2.png" alt=""/></span>
                    <h4>空间</h4>
                    <p>百度空间是一个轻松记录、分享生活的内容社区，在这里你可以找到更多志同道合的人，随时随地与好友保持沟通、一起找寻快乐。百度空间，让世界发现你的存在，共享你的精彩！</p>
                </li>
                <li class="m-list clearfix wenku">
                    <span><img src="/img/v2/icon3.png" alt=""/></span>
                    <h4>文库</h4>
                    <p>在线互动式文档分享平台，在这里，您可以和千万网友分享自己手中的文档，全文阅读其他用户的文档，同时，也可以利用分享文档获取的积分下载文档。</p>
                </li>
            </ul>
        </div>
        <div class="grid-25 right">
        <div class="passAcc"> 
            <div class="passAccInfo">
                <p class="accTab" id="acc_tab">
                    <span id="tab_nor" class="tab nor current"><a>普通登录</a></span>
                    <span id="tab_mob" class="tab mob"><a>手机登录</a></span>
                </p>
                <div class="passAccForm">
					<div id="loginForm">
					</div>
                </div>
                <div class="passAccReg">
                    <span>还没有百度帐号？<a class="reg_link" href="https://passport.baidu.com/v2/?reg&tpl=pp&u=" target="_blank">立即注册</a></span>
                </div>
            </div>
        </div>
        <div class="question">
            <h4>常见问题</h4>
            <ul>
                <li><a href="http://www.baidu.com/search/passport_help.html#06" target="_blank">如何设置更安全的密码？</a></li>
                <li><a href="http://www.baidu.com/search/passport_help.html#03" target="_blank">如何找回密码？</a></li>
                <li><a href="http://www.baidu.com/search/passport_help.html#02" target="_blank">如何修改我的密码？</a></li>
                <li><a href="http://www.baidu.com/search/passport_help.html#01" target="_blank">如何管理修改我的个人资料？</a></li>
                <li><a href="http://www.baidu.com/search/passport_help.html#07" target="_blank">如何使用消息功能？</a></li>
                <li><a href="http://www.baidu.com/search/passport_help.html#08" target="_blank">什么是安全登录？什么是安全控件</a></li>
            </ul>
        </div>
        </div>
    </div>
    
    <div id="footer">&copy;2013 Baidu</div>
</div>
<script type="text/javascript">
	var _config = {
		u:''
		,noreal_u:''
		,staticpage: 'https://passport.baidu.com/v3Jump.html'
	}
	var login_rem_name = '';
	if((document.charset.toLowerCase().indexOf('utf') == -1) && (navigator.userAgent.indexOf("MSIE") > 0)) {
		location.href = location.href + (location.href.indexOf('?')>-1? "&nocache=1": "?nocache=1");
	}
</script>
<script type="text/javascript" src="/js/magic-suggestion.js?cdnversion=20130110"></script>
<script type="text/javascript" src="/js/v3LoginPage.js?cdnversion=20130110"></script>
</body>
</html>