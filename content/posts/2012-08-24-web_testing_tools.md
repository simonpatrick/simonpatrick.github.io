---
layout: post
title: "Web Testing Tools list"
modified:
categories: [tools]
excerpt:
tags: [tools]
image: communication-icons-black-and-white-vector.jpg
date: 2012-09-24T10:31:11
---

#1. Cross Browser(浏览器兼容性测试)

### Why

	无数的浏览器，无数的版本，无数的终端。。。。。。。 这个理由就足够需要做兼容性测试了
	测试的悲剧就是这样的，听上去很简单，做起来就要人命，还被人不理解。。。。。。

### How

	* 自动化测试：自己写截屏工具，自己比较（需要进一步研究）
		1. sikuli
		2. selenium
		3. http://testingbot.com
		4. http://saucelabs.com
	* 网站：http://browsershots.org （自己没有验证要如何处理）
	* 标准检查：http://validator.w3.org
	* 浏览器分类
		1. WebKit：Chrome/Safari
		2. Grecko: Firefox
		3. Trident rendering engine: IE

#2. Web Accessibility

### Why
	更好的使用，更多的有意义的标示

### How
This simplest way to check against W3C compliance would be to open up Firefox, install the accessibility checker plug in, open your site to be tested and run a quick scan.
Tips:

	*  Firefox accessibility extension - https://addons.mozilla.org/en-US/firefox/addon/accessibility-evaluation-toolb/
	*  Tips on how best to describe the alt attribute -http://webdesign.about.com/od/beginningtutorials/a/aa122004.htm
	* The W3 standards on accessibility - http://www.w3.org/standards/webdesign/accessibility
	* Test Partners accessibility testing - http://www.testpartners.co.uk/accessibility_testing.htm

#3. Is the HTML valid?

### Why
  标准化，避免不必要的bug

### How

  * http://validator.w3.org
  * Firefox 插件
  * Good post on why you should validate - http://www.stevefenton.co.uk/Content/Blog/Date/201108/Blog/Do-I- Need-To-Validate-My-HTML
  * FireWeasel - https://addons.mozilla.org/en-US/firefox/addon/fireweasel/

#4. Check for Dead-links

### Why
 保证网站的最新内容，避免过时信息已经的误解。

### How

  * Link Check Tool: Xenu
  * Xenu Link Checker - http://home.snafu.de/tilman/xenulink.html
  * W3C Checker - http://validator.w3.org/checklink
  * Broken Link Checker Tool - http://www.brokenlinkcheck.com/

#5. One, Two, Many

### Why
	网站总是有一定并发的，所以可以先使用一个用户测试基本功能，然后使用两个用户检查是否存在简单的并发问题，最后就考虑使用压力测试工具。 这个方法简单的避免一些简单的并发问题

### How

	* JMeter -> webservice

#6. Multiple tabs and windows

### Why
	主要为了查看安全问题，数据刷新问题已经多cookie的问题

### How

	* example 1:
		Open Firefox and in one tab log in to your secure application.
		Then right click on a page and open that new page in a new tab. Both tabs are now considered to be in the same session.
		Now log out of the application in Tab 2 and try to perform some actions in Tab 1.
		Has it logged you out or let you perform an action?
		In most situations it would have logged you out.
		In many instances it is possible to log in to two different accounts in the same browser and end up sharing data across both tabs because of cross authentication.

	* example 2：
		I log in to my banking application in Tab 1 as Rob and then in Tab 2 as Dave.
		Now when I switch to tab 1 and follow a new link I might get to see Dave’s information.
		In Tab 2, Dave might even get to see my data.
		This is because of confused session data stored in a single cookie for the browser, which is shared between two tabs.
		It’s not just about authentication though.
		What about adding things to a shopping basket in multiple tabs – do they persist in the basket? What about state changes in your application across several tabs?
		Can I login across several browsers in different sessions?
		Can I trick browser side validation and restrictions by performing actions across a number of tabs?
		The best way to test in multiple browser tabs and sessions is to explore the application with multiple tabs open, checking what effect a change in one tab can have on the other.
		As you explore around look for data, states and actions that might be confused by bad cookie management, session management and cross tab problems.

	* Good site about cookies and sessions - http://www.allaboutcookies.org/cookies/session-cookies-used-for.html
	* Session Hijacking - http://en.wikipedia.org/wiki/Session_hijacking
	* Security implications of cookies - http://it.toolbox.com/blogs/securitymonkey/successful-hacking-with-xss- cookies-session-ids-11098
	* Burpsuite - http://portswigger.net/burp/
	* Firecookie - https://addons.mozilla.org/en-us/firefox/addon/firecookie/

#7. Http and Https

### Why
	敏感信息如果泄露，容易被人攻击，所以需要检查是否使用了http传输了敏感信息，同时有些信息被修改了是否会引起错误，比如http header，或者post数据。。。。。。

### How

	* 使用proxy工具：Burpsuite,Charles Proxy/Fiddler 查看请求和返回信息，修改请求信息看是否可以造成问题，比如修改了页面的某个价格，是否还是新价格购买成功；个人信息是否在里面；
	* Good security for web checklist –
	http://www.techrepublic.com/blog/security/ensure-basic-web-site-security-with-this-checklist/424
	* Differences between http and https - http://www.virtu-software.com/ask-doug/QandA.asp?q=7
	* Another differences post - http://www.wisegeek.com/what-is-the-difference-between-http-and-https.htm
	* Burpsuite - http://portswigger.net/burp/

#8. Client/Server Watch

### Why
	Web测试仅仅查看页面是远远不够的，所以测试需要知道送出去的请求是什么，得到的返回是什么。以下问题可能需要问以下：

	 Is the data being sent and received correct?
	 Is the layout working as expected?
	 Are the response times satisfactory?
	 How do timeouts affect the site?
	 Are there any errors in the code?
	 What happens if I pass in X?
	 What happens if I remove X?
	 What happens if the message is lost completely?

### How

	* Charles Proxy - http://www.charlesproxy.com/
	* Fiddler - http://fiddler2.com/fiddler2/
	* Firebug - http://getfirebug.com/
	* Firecookie - https://addons.mozilla.org/en-US/firefox/addon/firecookie/

#9. Security

### Why
  不用多少，听听各种脱库事件就知道了，只是我的能力够吗？：）

### How

	* Burpsuite - http://portswigger.net/burp/
	* Web Scarab - https://www.owasp.org/index.php/WebScarab_Getting_Started
	* Web Hackers book - http://www.amazon.co.uk/Web-Application-Hackers-Handbook- Discovering/dp/0470170778
	* OWASP Top Ten - https://www.owasp.org/index.php/Category:OWASP_Top_Ten_Project
	* Plynt Security Testing Experts - http://www.plynt.com/
	* Salesforce Burpsuite for App Exchange Partners - http://security.force.com/webappscanner
	* Start with the treat profile - http://www.securityalliance.co.uk/blog/bid/40335/Web-Application-Security-Testing-Start-with-the-Threat-Profile
	* Firefox add-ons (search for “security”)- https://addons.mozilla.org/en-US/firefox/

#10. Browser Extentions

* Selenium IDE http://seleniumhq.org/projects/ide/
Selenium is fast becoming an industry standard tool. This is the IDE version. Visit http://seleniumhq.org/ for more information on other tools in the set like Selenium Grid.
* IE Tab https://addons.mozilla.org/en-US/firefox/addon/1419 Flips your Firefox tab in to Internet Explorer mode.
* https://addons.mozilla.org/en-US/firefox/addon/5792 Re-sizes your window to different screen sizes
* Fire cookie https://addons.mozilla.org/en-US/firefox/addon/6683 Lets you to see and manage cookies through the Firebug add-on.
* Delicious https://addons.mozilla.org/en-US/firefox/addon/3615
* Social bookmarking service. Never lose a site of interest again and share them with the community too. Perfect for bookmarking testing sites, information, snippets and blogs.
* Clear Cache https://addons.mozilla.org/en-US/firefox/addon/1801 Clears out the cache within the browser at the click of a button.
* Copy Plain Text https://addons.mozilla.org/en-US/firefox/addon/134
Copies any text from the browser in to a plain text format losing all formatting.
* Fiddler Hook http://www.fiddler2.com/fiddler2/addons/fiddlerhook/ Firefox add-on for integrating with Fiddler (a debugging tool).
* Download Status https://addons.mozilla.org/en-US/firefox/addon/26
Shows your downloads in a toolbar at the bottom of the browser window. Keeps it nice and tidy and easy access to your downloads.
* Xmarks https://addons.mozilla.org/en-US/firefox/addon/2410
* Allow you to save your bookmarks and sync them between browsers on different machines. Works across browsers too. This is great if you test on several different machines. It means you can save your bookmarks once and find them on other browsers you have synched.
* W3C Page Validator https://addons.mozilla.org/en-US/firefox/addon/2250
 Check your page against W3C standards and compliance.
* Pencil https://addons.mozilla.org/en-US/firefox/addon/8487
Great for screen mocks and notes.
* SQL Injection https://addons.mozilla.org/en-US/firefox/addon/6727
* Quick Restart https://addons.mozilla.org/en-US/firefox/addon/3559
* Restarts Firefox maintaining all tabs and open docs when it launches it again.
* Firebug https://addons.mozilla.org/en-US/firefox/addon/1843 How can you test websites without this one?
* Regular Expressions Tester https://addons.mozilla.org/en-US/firefox/addon/2077 Tool for testing regular expressions.
* Quick Locale Switcher https://addons.mozilla.org/en-US/firefox/addon/1333
* Good extension allowing for quick switching between browser locales.
 Http Fox https://addons.mozilla.org/en-US/firefox/addon/6647
* Good tool for analyzing the http traffic through your browser.
* TAW3 https://addons.mozilla.org/en-US/firefox/addon/1158?src=api
* Accessibility checking tool. Awesome.
* Firefox Accessibility Tools https://addons.mozilla.org/en-US/firefox/addon/5809?src=api Accessibility compliance checking tool.

### Back to the benginging again

* Stack Overflow question on disabling back capability (which you cannot by the way) -
* http://stackoverflow.com/questions/7816195/how-to-disable-back-button-in-browser-when-user-logout-in- classic-asp
* IE security problem with the Back Button.
* http://www.wired.com/science/discoveries/news/2002/04/51899?currentPage=all

### 其他的一些测试方式

* Change the URL
* Tab Order
* See the Source
* UX
		* Customer Support
		* Release Notes
		* Error Tolernt
		* Documentation
		* Performance
		* Security
		* Usability and Ease to Use
		* Accessibility
* Change the locale
* Resize the windows and resolution
* Block pop-ups
* Disable CSS
* Text Only
* Disable Javascript
* Refresh during page loads
* Check SEO
* Five second test
* Throttle It (限流处理)

### 兼容性测试

[support detail](www.supportdetails.com)
[adobe flash version](http://www.adobe.com/software/flash/about/).
[java version](java.com/en/download/installed.jsp)
### 工具
[video record](http://www.techsmith.com/download/jing/)[FastStone Capture](http://faststone.org/FSCaptureDetail.htm)
[test data](http://www.xtra-rant.com/gennames/)
[test data tool](http://www.markrichman.com/2007/09/26/generating-random-names-as-test-data/)
[perlclip test-data](http://www.satisfice.com/tools.shtml)
[combination tools](http://hexawise.com/)
[Rapid Reporter](http://testing.gershon.info/reporter/. )

### 自动化测试工具

- SauceLabs
- BrowserStack
