#encoding: utf-8

from lxml import etree

text = """
    <!--主体main-->
    <div id="main" class="inner home-inner">
        <div class="home-box">
            <div class="home-sider">
                <!-- 左侧职位选择 -->
                <div class="job-menu">
                        <dl class="">
                            <dd>
                                <i class="icon-arrow-right"></i>
                                <b>技术</b>
                                    <a href="/c101210100-p100101/">Java</a>
                                    <a href="/c101210100-p100103/">PHP</a>
                                    <a href="/c101210100-p100901/">web前端</a>
                                    <a href="/c101210100-p100120/">算法工程师</a>
                            </dd>
                            <div class="menu-line"></div>
                            <div class="menu-sub">
                                <p class="menu-article">技术</p>
                                <ul>
                                            <li>
                                                <h4>后端开发</h4>
                                                <div class="text">
                                                            <a ka="search_100199" href="/c101210100-p100199/">后端开发</a>
                                                            <a ka="search_100101" href="/c101210100-p100101/">Java</a>
                                                            <a ka="search_100102" href="/c101210100-p100102/">C++</a>
                                                            <a ka="search_100103" href="/c101210100-p100103/">PHP</a>
                                                            <a ka="search_100104" href="/c101210100-p100104/">数据挖掘</a>
                                                            <a ka="search_100105" href="/c101210100-p100105/">C</a>
                                                            <a ka="search_100106" href="/c101210100-p100106/">C#</a>
                                                            <a ka="search_100107" href="/c101210100-p100107/">.NET</a>
                                                            <a ka="search_100108" href="/c101210100-p100108/">Hadoop</a>
                                                            <a ka="search_100109" href="/c101210100-p100109/">Python</a>
                                                            <a ka="search_100110" href="/c101210100-p100110/">Delphi</a>
                                                            <a ka="search_100111" href="/c101210100-p100111/">VB</a>
                                                            <a ka="search_100112" href="/c101210100-p100112/">Perl</a>
                                                            <a ka="search_100113" href="/c101210100-p100113/">Ruby</a>
                                                            <a ka="search_100114" href="/c101210100-p100114/">Node.js</a>
                                                            <a ka="search_100115" href="/c101210100-p100115/">搜索算法</a>
                                                            <a ka="search_100116" href="/c101210100-p100116/">Golang</a>
                                                            <a ka="search_100117" href="/c101210100-p100117/">自然语言处理</a>
                                                            <a ka="search_100118" href="/c101210100-p100118/">推荐算法</a>
                                                            <a ka="search_100119" href="/c101210100-p100119/">Erlang</a>
                                                            <a ka="search_100120" href="/c101210100-p100120/">算法工程师</a>
                                                            <a ka="search_100121" href="/c101210100-p100121/">语音/视频/图形开发</a>
                                                            <a ka="search_100122" href="/c101210100-p100122/">数据采集</a>
                                                </div>
                                            </li>
                                            <li>
                                                <h4>移动开发</h4>
                                                <div class="text">
                                                            <a ka="search_100299" href="/c101210100-p100299/">移动开发</a>
                                                            <a ka="search_100201" href="/c101210100-p100201/">HTML5</a>
                                                            <a ka="search_100202" href="/c101210100-p100202/">Android</a>
                                                            <a ka="search_100203" href="/c101210100-p100203/">iOS</a>
                                                            <a ka="search_100204" href="/c101210100-p100204/">WP</a>
                                                            <a ka="search_100205" href="/c101210100-p100205/">移动web前端</a>
                                                            <a ka="search_100206" href="/c101210100-p100206/">Flash开发</a>
                                                            <a ka="search_100208" href="/c101210100-p100208/">JavaScript</a>
                                                            <a ka="search_100209" href="/c101210100-p100209/">U3D</a>
                                                            <a ka="search_100210" href="/c101210100-p100210/">COCOS2DX</a>
                                                </div>
                                            </li>
                                            <li>
                                                <h4>测试</h4>
                                                <div class="text">
                                                            <a ka="search_100301" href="/c101210100-p100301/">测试工程师</a>
                                                            <a ka="search_100302" href="/c101210100-p100302/">自动化测试</a>
                                                            <a ka="search_100303" href="/c101210100-p100303/">功能测试</a>
                                                            <a ka="search_100304" href="/c101210100-p100304/">性能测试</a>
                                                            <a ka="search_100305" href="/c101210100-p100305/">测试开发</a>
                                                            <a ka="search_100306" href="/c101210100-p100306/">移动端测试</a>
                                                            <a ka="search_100307" href="/c101210100-p100307/">游戏测试</a>
                                                            <a ka="search_100308" href="/c101210100-p100308/">硬件测试</a>
                                                            <a ka="search_100309" href="/c101210100-p100309/">软件测试</a>
                                                </div>
                                            </li>
                                            <li>
                                                <h4>运维/技术支持</h4>
                                                <div class="text">
                                                            <a ka="search_100401" href="/c101210100-p100401/">运维工程师</a>
                                                            <a ka="search_100402" href="/c101210100-p100402/">运维开发工程师</a>
                                                            <a ka="search_100403" href="/c101210100-p100403/">网络工程师</a>
                                                            <a ka="search_100404" href="/c101210100-p100404/">系统工程师</a>
                                                            <a ka="search_100405" href="/c101210100-p100405/">IT技术支持</a>
                                                            <a ka="search_100406" href="/c101210100-p100406/">系统管理员</a>
                                                            <a ka="search_100407" href="/c101210100-p100407/">网络安全</a>
                                                            <a ka="search_100408" href="/c101210100-p100408/">系统安全</a>
                                                            <a ka="search_100409" href="/c101210100-p100409/">DBA</a>
                                                </div>
                                            </li>
                                            <li>
                                                <h4>数据</h4>
                                                <div class="text">
                                                            <a ka="search_100599" href="/c101210100-p100599/">数据</a>
                                                            <a ka="search_100506" href="/c101210100-p100506/">ETL工程师</a>
                                                            <a ka="search_100507" href="/c101210100-p100507/">数据仓库</a>
                                                            <a ka="search_100508" href="/c101210100-p100508/">数据开发</a>
                                                            <a ka="search_100509" href="/c101210100-p100509/">数据挖掘</a>
                                                            <a ka="search_100511" href="/c101210100-p100511/">数据分析师</a>
                                                            <a ka="search_100512" href="/c101210100-p100512/">数据架构师</a>
                                                            <a ka="search_100513" href="/c101210100-p100513/">算法研究员</a>
                                                </div>
                                            </li>
                                            <li>
                                                <h4>项目管理</h4>
                                                <div class="text">
                                                            <a ka="search_100601" href="/c101210100-p100601/">项目经理</a>
                                                            <a ka="search_100602" href="/c101210100-p100602/">项目主管</a>
                                                            <a ka="search_100603" href="/c101210100-p100603/">项目助理</a>
                                                            <a ka="search_100604" href="/c101210100-p100604/">项目专员</a>
                                                            <a ka="search_100605" href="/c101210100-p100605/">实施顾问</a>
                                                            <a ka="search_100606" href="/c101210100-p100606/">实施工程师</a>
                                                            <a ka="search_100607" href="/c101210100-p100607/">需求分析工程师</a>
                                                </div>
                                            </li>
                                            <li>
                                                <h4>硬件开发</h4>
                                                <div class="text">
                                                            <a ka="search_100801" href="/c101210100-p100801/">硬件</a>
                                                            <a ka="search_100802" href="/c101210100-p100802/">嵌入式</a>
                                                            <a ka="search_100803" href="/c101210100-p100803/">自动化</a>
                                                            <a ka="search_100804" href="/c101210100-p100804/">单片机</a>
                                                            <a ka="search_100805" href="/c101210100-p100805/">电路设计</a>
                                                            <a ka="search_100806" href="/c101210100-p100806/">驱动开发</a>
                                                            <a ka="search_100807" href="/c101210100-p100807/">系统集成</a>
                                                            <a ka="search_100808" href="/c101210100-p100808/">FPGA开发</a>
                                                            <a ka="search_100809" href="/c101210100-p100809/">DSP开发</a>
                                                            <a ka="search_100810" href="/c101210100-p100810/">ARM开发</a>
                                                            <a ka="search_100811" href="/c101210100-p100811/">PCB工艺</a>
                                                            <a ka="search_100812" href="/c101210100-p100812/">模具设计</a>
                                                            <a ka="search_100813" href="/c101210100-p100813/">热传导</a>
                                                            <a ka="search_100814" href="/c101210100-p100814/">材料工程师</a>
                                                            <a ka="search_100815" href="/c101210100-p100815/">精益工程师</a>
                                                            <a ka="search_100816" href="/c101210100-p100816/">射频工程师</a>
                                                </div>
                                            </li>
                                            <li>
                                                <h4>前端开发</h4>
                                                <div class="text">
                                                            <a ka="search_100999" href="/c101210100-p100999/">前端开发</a>
                                                            <a ka="search_100901" href="/c101210100-p100901/">web前端</a>
                                                            <a ka="search_100902" href="/c101210100-p100902/">JavaScript</a>
                                                            <a ka="search_100903" href="/c101210100-p100903/">Flash开发</a>
                                                            <a ka="search_100904" href="/c101210100-p100904/">HTML5</a>
                                                </div>
                                            </li>
                                            <li>
                                                <h4>通信</h4>
                                                <div class="text">
                                                            <a ka="search_101001" href="/c101210100-p101001/">通信技术工程师</a>
                                                            <a ka="search_101002" href="/c101210100-p101002/">通信研发工程师</a>
                                                            <a ka="search_101003" href="/c101210100-p101003/">数据通信工程师</a>
                                                            <a ka="search_101004" href="/c101210100-p101004/">移动通信工程师</a>
                                                            <a ka="search_101005" href="/c101210100-p101005/">电信网络工程师</a>
                                                            <a ka="search_101006" href="/c101210100-p101006/">电信交换工程师</a>
                                                            <a ka="search_101007" href="/c101210100-p101007/">有线传输工程师</a>
                                                            <a ka="search_101008" href="/c101210100-p101008/">无线射频工程师</a>
                                                            <a ka="search_101009" href="/c101210100-p101009/">通信电源工程师</a>
                                                            <a ka="search_101010" href="/c101210100-p101010/">通信标准化工程师</a>
                                                            <a ka="search_101011" href="/c101210100-p101011/">通信项目专员</a>
                                                            <a ka="search_101012" href="/c101210100-p101012/">通信项目经理</a>
                                                            <a ka="search_101013" href="/c101210100-p101013/">核心网工程师</a>
                                                            <a ka="search_101014" href="/c101210100-p101014/">通信测试工程师</a>
                                                            <a ka="search_101015" href="/c101210100-p101015/">通信设备工程师</a>
                                                            <a ka="search_101016" href="/c101210100-p101016/">光通信工程师</a>
                                                            <a ka="search_101017" href="/c101210100-p101017/">光传输工程师</a>
                                                            <a ka="search_101018" href="/c101210100-p101018/">光网络工程师</a>
                                                </div>
                                            </li>
                                            <li>
                                                <h4>电子/半导体</h4>
                                                <div class="text">
                                                            <a ka="search_101401" href="/c101210100-p101401/">电子工程师</a>
                                                            <a ka="search_101402" href="/c101210100-p101402/">电气工程师</a>
                                                            <a ka="search_101403" href="/c101210100-p101403/">FAE</a>
                                                            <a ka="search_101404" href="/c101210100-p101404/">电气设计工程师</a>
                                                </div>
                                            </li>
                                            <li>
                                                <h4>高端技术职位</h4>
                                                <div class="text">
                                                            <a ka="search_100799" href="/c101210100-p100799/">高端技术职位</a>
                                                            <a ka="search_100701" href="/c101210100-p100701/">技术经理</a>
                                                            <a ka="search_100702" href="/c101210100-p100702/">技术总监</a>
                                                            <a ka="search_100703" href="/c101210100-p100703/">测试经理</a>
                                                            <a ka="search_100704" href="/c101210100-p100704/">架构师</a>
                                                            <a ka="search_100705" href="/c101210100-p100705/">CTO</a>
                                                            <a ka="search_100706" href="/c101210100-p100706/">运维总监</a>
                                                            <a ka="search_100707" href="/c101210100-p100707/">技术合伙人</a>
                                                </div>
                                            </li>
                                            <li>
                                                <h4>人工智能</h4>
                                                <div class="text">
                                                            <a ka="search_101399" href="/c101210100-p101399/">人工智能</a>
                                                            <a ka="search_101301" href="/c101210100-p101301/">机器学习</a>
                                                            <a ka="search_101302" href="/c101210100-p101302/">深度学习</a>
                                                            <a ka="search_101303" href="/c101210100-p101303/">图像算法</a>
                                                            <a ka="search_101304" href="/c101210100-p101304/">图像处理</a>
                                                            <a ka="search_101305" href="/c101210100-p101305/">语音识别</a>
                                                            <a ka="search_101306" href="/c101210100-p101306/">图像识别</a>
                                                            <a ka="search_101307" href="/c101210100-p101307/">算法研究员</a>
                                                </div>
                                            </li>
                                            <li>
                                                <h4>软件销售支持</h4>
                                                <div class="text">
                                                            <a ka="search_101299" href="/c101210100-p101299/">软件销售支持</a>
                                                            <a ka="search_101201" href="/c101210100-p101201/">售前工程师</a>
                                                            <a ka="search_101202" href="/c101210100-p101202/">售后工程师</a>
                                                </div>
                                            </li>
                                            <li>
                                                <h4>其他技术职位</h4>
                                                <div class="text">
                                                            <a ka="search_101101" href="/c101210100-p101101/">其他技术职位</a>
                                                </div>
                                            </li>
                                </ul>
                            </div>
                        </dl>
                        <dl class="">
                            <dd>
                                <i class="icon-arrow-right"></i>
                                <b>产品</b>
                                    <a href="/c101210100-p110101/">产品经理</a>
                                    <a href="/c101210100-p110302/">产品总监</a>
                                    <a href="/c101210100-p110105/">数据产品经理</a>
                            </dd>
                            <div class="menu-line"></div>
                            <div class="menu-sub">
                                <p class="menu-article">产品</p>
                                <ul>
                                            <li>
                                                <h4>产品经理</h4>
                                                <div class="text">
                                                            <a ka="search_110101" href="/c101210100-p110101/">产品经理</a>
                                                            <a ka="search_110102" href="/c101210100-p110102/">网页产品经理</a>
                                                            <a ka="search_110103" href="/c101210100-p110103/">移动产品经理</a>
                                                            <a ka="search_110104" href="/c101210100-p110104/">产品助理</a>
                                                            <a ka="search_110105" href="/c101210100-p110105/">数据产品经理</a>
                                                            <a ka="search_110106" href="/c101210100-p110106/">电商产品经理</a>
                                                            <a ka="search_110107" href="/c101210100-p110107/">游戏策划</a>
                                                            <a ka="search_110108" href="/c101210100-p110108/">产品专员</a>
                                                </div>
                                            </li>
                                            <li>
                                                <h4>高端产品职位</h4>
                                                <div class="text">
                                                            <a ka="search_110399" href="/c101210100-p110399/">高端产品职位</a>
                                                            <a ka="search_110302" href="/c101210100-p110302/">产品总监</a>
                                                            <a ka="search_110303" href="/c101210100-p110303/">游戏制作人</a>
                                                            <a ka="search_110304" href="/c101210100-p110304/">产品VP</a>
                                                </div>
                                            </li>
                                            <li>
                                                <h4>其他产品职位</h4>
                                                <div class="text">
                                                            <a ka="search_110401" href="/c101210100-p110401/">其他产品职位</a>
                                                </div>
                                            </li>
                                </ul>
                            </div>
                        </dl>
                        <dl class="">
                            <dd>
                                <i class="icon-arrow-right"></i>
                                <b>设计</b>
                                    <a href="/c101210100-p120105/">UI设计师</a>
                                    <a href="/c101210100-p120106/">平面设计师</a>
                                    <a href="/c101210100-p120201/">交互设计师</a>
                            </dd>
                            <div class="menu-line"></div>
                            <div class="menu-sub">
                                <p class="menu-article">设计</p>
                                <ul>
                                            <li>
                                                <h4>视觉设计</h4>
                                                <div class="text">
                                                            <a ka="search_120199" href="/c101210100-p120199/">视觉设计</a>
                                                            <a ka="search_120101" href="/c101210100-p120101/">视觉设计师</a>
                                                            <a ka="search_120102" href="/c101210100-p120102/">网页设计师</a>
                                                            <a ka="search_120103" href="/c101210100-p120103/">Flash设计师</a>
                                                            <a ka="search_120104" href="/c101210100-p120104/">APP设计师</a>
                                                            <a ka="search_120105" href="/c101210100-p120105/">UI设计师</a>
                                                            <a ka="search_120106" href="/c101210100-p120106/">平面设计师</a>
                                                            <a ka="search_120107" href="/c101210100-p120107/">美术设计师（2D/3D）</a>
                                                            <a ka="search_120108" href="/c101210100-p120108/">广告设计师</a>
                                                            <a ka="search_120109" href="/c101210100-p120109/">多媒体设计师</a>
                                                            <a ka="search_120110" href="/c101210100-p120110/">原画师</a>
                                                            <a ka="search_120111" href="/c101210100-p120111/">游戏特效</a>
                                                            <a ka="search_120112" href="/c101210100-p120112/">游戏界面设计师</a>
                                                            <a ka="search_120113" href="/c101210100-p120113/">游戏场景</a>
                                                            <a ka="search_120114" href="/c101210100-p120114/">游戏角色</a>
                                                            <a ka="search_120115" href="/c101210100-p120115/">游戏动作</a>
                                                            <a ka="search_120116" href="/c101210100-p120116/">三维/CAD/制图</a>
                                                            <a ka="search_120117" href="/c101210100-p120117/">美工</a>
                                                            <a ka="search_120118" href="/c101210100-p120118/">包装设计</a>
                                                            <a ka="search_120119" href="/c101210100-p120119/">设计师助理</a>
                                                            <a ka="search_120120" href="/c101210100-p120120/">动画设计师</a>
                                                            <a ka="search_120121" href="/c101210100-p120121/">插画师</a>
                                                </div>
                                            </li>
                                            <li>
                                                <h4>交互设计</h4>
                                                <div class="text">
                                                            <a ka="search_120201" href="/c101210100-p120201/">交互设计师</a>
                                                            <a ka="search_120202" href="/c101210100-p120202/">无线交互设计师</a>
                                                            <a ka="search_120203" href="/c101210100-p120203/">网页交互设计师</a>
                                                            <a ka="search_120204" href="/c101210100-p120204/">硬件交互设计师</a>
                                                </div>
                                            </li>
                                            <li>
                                                <h4>用户研究</h4>
                                                <div class="text">
                                                            <a ka="search_120301" href="/c101210100-p120301/">数据分析师</a>
                                                            <a ka="search_120302" href="/c101210100-p120302/">用户研究员</a>
                                                            <a ka="search_120303" href="/c101210100-p120303/">游戏数值策划</a>
                                                            <a ka="search_120304" href="/c101210100-p120304/">UX设计师</a>
                                                            <a ka="search_120407" href="/c101210100-p120407/">用户研究经理</a>
                                                            <a ka="search_120408" href="/c101210100-p120408/">用户研究总监</a>
                                                </div>
                                            </li>
                                            <li>
                                                <h4>高端设计职位</h4>
                                                <div class="text">
                                                            <a ka="search_120499" href="/c101210100-p120499/">高端设计职位</a>
                                                            <a ka="search_120401" href="/c101210100-p120401/">设计经理/主管</a>
                                                            <a ka="search_120402" href="/c101210100-p120402/">设计总监</a>
                                                            <a ka="search_120403" href="/c101210100-p120403/">视觉设计经理</a>
                                                            <a ka="search_120404" href="/c101210100-p120404/">视觉设计总监</a>
                                                            <a ka="search_120405" href="/c101210100-p120405/">交互设计经理/主管</a>
                                                            <a ka="search_120406" href="/c101210100-p120406/">交互设计总监</a>
                                                </div>
                                            </li>
                                            <li>
                                                <h4>非视觉设计</h4>
                                                <div class="text">
                                                            <a ka="search_120699" href="/c101210100-p120699/">非视觉设计</a>
                                                            <a ka="search_120601" href="/c101210100-p120601/">服装设计</a>
                                                            <a ka="search_120602" href="/c101210100-p120602/">工业设计</a>
                                                            <a ka="search_120603" href="/c101210100-p120603/">橱柜设计</a>
                                                            <a ka="search_120604" href="/c101210100-p120604/">家具设计</a>
                                                            <a ka="search_120605" href="/c101210100-p120605/">家居设计</a>
                                                            <a ka="search_120606" href="/c101210100-p120606/">珠宝设计</a>
                                                            <a ka="search_120607" href="/c101210100-p120607/">室内设计</a>
                                                            <a ka="search_120608" href="/c101210100-p120608/">陈列设计</a>
                                                            <a ka="search_120610" href="/c101210100-p120610/">景观设计</a>
                                                </div>
                                            </li>
                                            <li>
                                                <h4>其他设计职位</h4>
                                                <div class="text">
                                                            <a ka="search_120501" href="/c101210100-p120501/">其他设计职位</a>
                                                </div>
                                            </li>
                                </ul>
                            </div>
                        </dl>
                        <dl class="">
                            <dd>
                                <i class="icon-arrow-right"></i>
                                <b>运营</b>
                                    <a href="/c101210100-p130111/">新媒体运营</a>
                                    <a href="/c101210100-p130102/">产品运营</a>
                                    <a href="/c101210100-p130109/">网络推广</a>
                            </dd>
                            <div class="menu-line"></div>
                            <div class="menu-sub">
                                <p class="menu-article">运营</p>
                                <ul>
                                            <li>
                                                <h4>运营</h4>
                                                <div class="text">
                                                            <a ka="search_130199" href="/c101210100-p130199/">运营</a>
                                                            <a ka="search_130101" href="/c101210100-p130101/">用户运营</a>
                                                            <a ka="search_130102" href="/c101210100-p130102/">产品运营</a>
                                                            <a ka="search_130103" href="/c101210100-p130103/">数据运营</a>
                                                            <a ka="search_130104" href="/c101210100-p130104/">内容运营</a>
                                                            <a ka="search_130105" href="/c101210100-p130105/">活动运营</a>
                                                            <a ka="search_130106" href="/c101210100-p130106/">商家运营</a>
                                                            <a ka="search_130107" href="/c101210100-p130107/">品类运营</a>
                                                            <a ka="search_130108" href="/c101210100-p130108/">游戏运营</a>
                                                            <a ka="search_130109" href="/c101210100-p130109/">网络推广</a>
                                                            <a ka="search_130110" href="/c101210100-p130110/">网站运营</a>
                                                            <a ka="search_130111" href="/c101210100-p130111/">新媒体运营</a>
                                                            <a ka="search_130112" href="/c101210100-p130112/">社区运营</a>
                                                            <a ka="search_130113" href="/c101210100-p130113/">微信运营</a>
                                                            <a ka="search_130114" href="/c101210100-p130114/">微博运营</a>
                                                            <a ka="search_130115" href="/c101210100-p130115/">策略运营</a>
                                                            <a ka="search_130116" href="/c101210100-p130116/">线下拓展运营</a>
                                                            <a ka="search_130117" href="/c101210100-p130117/">电商运营</a>
                                                            <a ka="search_130118" href="/c101210100-p130118/">运营助理/专员</a>
                                                            <a ka="search_130120" href="/c101210100-p130120/">内容审核</a>
                                                            <a ka="search_130119" href="/c101210100-p130119/">销售运营</a>
                                                </div>
                                            </li>
                                            <li>
                                                <h4>编辑</h4>
                                                <div class="text">
                                                            <a ka="search_130299" href="/c101210100-p130299/">编辑</a>
                                                            <a ka="search_130201" href="/c101210100-p130201/">副主编</a>
                                                            <a ka="search_130202" href="/c101210100-p130202/">内容编辑</a>
                                                            <a ka="search_130203" href="/c101210100-p130203/">文案策划</a>
                                                            <a ka="search_130204" href="/c101210100-p130204/">网站编辑</a>
                                                            <a ka="search_130205" href="/c101210100-p130205/">记者</a>
                                                            <a ka="search_130206" href="/c101210100-p130206/">采编</a>
                                                </div>
                                            </li>
                                            <li>
                                                <h4>客服</h4>
                                                <div class="text">
                                                            <a ka="search_130301" href="/c101210100-p130301/">售前咨询</a>
                                                            <a ka="search_130302" href="/c101210100-p130302/">售后咨询</a>
                                                            <a ka="search_130303" href="/c101210100-p130303/">网络客服</a>
                                                            <a ka="search_130304" href="/c101210100-p130304/">客服经理</a>
                                                            <a ka="search_130305" href="/c101210100-p130305/">客服专员/助理</a>
                                                            <a ka="search_130306" href="/c101210100-p130306/">客服主管</a>
                                                            <a ka="search_130307" href="/c101210100-p130307/">客服总监</a>
                                                            <a ka="search_130308" href="/c101210100-p130308/">电话客服</a>
                                                            <a ka="search_130309" href="/c101210100-p130309/">咨询热线/呼叫中心客服</a>
                                                </div>
                                            </li>
                                            <li>
                                                <h4>高端运营职位</h4>
                                                <div class="text">
                                                            <a ka="search_130499" href="/c101210100-p130499/">高端运营职位</a>
                                                            <a ka="search_130401" href="/c101210100-p130401/">主编</a>
                                                            <a ka="search_130402" href="/c101210100-p130402/">运营总监</a>
                                                            <a ka="search_130403" href="/c101210100-p130403/">COO</a>
                                                            <a ka="search_130404" href="/c101210100-p130404/">客服总监</a>
                                                            <a ka="search_130405" href="/c101210100-p130405/">运营经理/主管</a>
                                                </div>
                                            </li>
                                            <li>
                                                <h4>其他运营职位</h4>
                                                <div class="text">
                                                            <a ka="search_130501" href="/c101210100-p130501/">其他运营职位</a>
                                                </div>
                                            </li>
                                </ul>
                            </div>
                        </dl>
                        <dl class="">
                            <dd>
                                <i class="icon-arrow-right"></i>
                                <b>市场</b>
                                    <a href="/c101210100-p140101/">市场营销</a>
                                    <a href="/c101210100-p140104/">市场推广</a>
                                    <a href="/c101210100-p140203/">品牌公关</a>
                                    <a href="/c101210100-p140604/">策划经理</a>
                            </dd>
                            <div class="menu-line"></div>
                            <div class="menu-sub">
                                <p class="menu-article">市场</p>
                                <ul>
                                            <li>
                                                <h4>市场/营销</h4>
                                                <div class="text">
                                                            <a ka="search_140114" href="/c101210100-p140114/">选址开发</a>
                                                            <a ka="search_140101" href="/c101210100-p140101/">市场营销</a>
                                                            <a ka="search_140102" href="/c101210100-p140102/">市场策划</a>
                                                            <a ka="search_140103" href="/c101210100-p140103/">市场顾问</a>
                                                            <a ka="search_140104" href="/c101210100-p140104/">市场推广</a>
                                                            <a ka="search_140105" href="/c101210100-p140105/">SEO</a>
                                                            <a ka="search_140106" href="/c101210100-p140106/">SEM</a>
                                                            <a ka="search_140107" href="/c101210100-p140107/">商务渠道</a>
                                                            <a ka="search_140108" href="/c101210100-p140108/">商业数据分析</a>
                                                            <a ka="search_140109" href="/c101210100-p140109/">活动策划</a>
                                                            <a ka="search_140110" href="/c101210100-p140110/">网络营销</a>
                                                            <a ka="search_140111" href="/c101210100-p140111/">海外市场</a>
                                                            <a ka="search_140112" href="/c101210100-p140112/">政府关系</a>
                                                            <a ka="search_140113" href="/c101210100-p140113/">APP推广</a>
                                                </div>
                                            </li>
                                            <li>
                                                <h4>公关媒介</h4>
                                                <div class="text">
                                                            <a ka="search_140299" href="/c101210100-p140299/">公关媒介</a>
                                                            <a ka="search_140201" href="/c101210100-p140201/">媒介经理</a>
                                                            <a ka="search_140202" href="/c101210100-p140202/">广告协调</a>
                                                            <a ka="search_140203" href="/c101210100-p140203/">品牌公关</a>
                                                            <a ka="search_140204" href="/c101210100-p140204/">媒介专员</a>
                                                            <a ka="search_140205" href="/c101210100-p140205/">活动策划执行</a>
                                                            <a ka="search_140206" href="/c101210100-p140206/">媒介策划</a>
                                                </div>
                                            </li>
                                            <li>
                                                <h4>会务会展</h4>
                                                <div class="text">
                                                            <a ka="search_140599" href="/c101210100-p140599/">会务会展</a>
                                                            <a ka="search_140501" href="/c101210100-p140501/">会议活动销售</a>
                                                            <a ka="search_140502" href="/c101210100-p140502/">会议活动策划</a>
                                                            <a ka="search_140503" href="/c101210100-p140503/">会议活动执行</a>
                                                            <a ka="search_140504" href="/c101210100-p140504/">会展活动销售</a>
                                                            <a ka="search_140505" href="/c101210100-p140505/">会展活动策划</a>
                                                            <a ka="search_140506" href="/c101210100-p140506/">会展活动执行</a>
                                                </div>
                                            </li>
                                            <li>
                                                <h4>广告</h4>
                                                <div class="text">
                                                            <a ka="search_140699" href="/c101210100-p140699/">广告</a>
                                                            <a ka="search_140601" href="/c101210100-p140601/">广告创意</a>
                                                            <a ka="search_140602" href="/c101210100-p140602/">美术指导</a>
                                                            <a ka="search_140603" href="/c101210100-p140603/">广告设计师</a>
                                                            <a ka="search_140604" href="/c101210100-p140604/">策划经理</a>
                                                            <a ka="search_140605" href="/c101210100-p140605/">文案</a>
                                                            <a ka="search_140607" href="/c101210100-p140607/">广告制作</a>
                                                            <a ka="search_140608" href="/c101210100-p140608/">媒介投放</a>
                                                            <a ka="search_140609" href="/c101210100-p140609/">媒介合作</a>
                                                            <a ka="search_140610" href="/c101210100-p140610/">媒介顾问</a>
                                                            <a ka="search_140611" href="/c101210100-p140611/">广告审核</a>
                                                </div>
                                            </li>
                                            <li>
                                                <h4>高端市场职位</h4>
                                                <div class="text">
                                                            <a ka="search_140499" href="/c101210100-p140499/">高端市场职位</a>
                                                            <a ka="search_140401" href="/c101210100-p140401/">市场总监</a>
                                                            <a ka="search_140404" href="/c101210100-p140404/">CMO</a>
                                                            <a ka="search_140405" href="/c101210100-p140405/">公关总监</a>
                                                            <a ka="search_140406" href="/c101210100-p140406/">媒介总监</a>
                                                            <a ka="search_140407" href="/c101210100-p140407/">创意总监</a>
                                                </div>
                                            </li>
                                            <li>
                                                <h4>其他市场职位</h4>
                                                <div class="text">
                                                            <a ka="search_140701" href="/c101210100-p140701/">其他市场职位</a>
                                                </div>
                                            </li>
                                </ul>
                            </div>
                        </dl>
                        <dl class="">
                            <dd>
                                <i class="icon-arrow-right"></i>
                                <b>人事</b>
                                    <a href="/c101210100-p150104/">人事/HR</a>
                                    <a href="/c101210100-p150204/">行政</a>
                                    <a href="/c101210100-p150303/">财务</a>
                                    <a href="/c101210100-p150105/">培训</a>
                                    <a href="/c101210100-p150107/">绩效考核</a>
                            </dd>
                            <div class="menu-line"></div>
                            <div class="menu-sub">
                                <p class="menu-article">人事</p>
                                <ul>
                                            <li>
                                                <h4>人力资源</h4>
                                                <div class="text">
                                                            <a ka="search_150101" href="/c101210100-p150101/">人力资源主管</a>
                                                            <a ka="search_150102" href="/c101210100-p150102/">招聘</a>
                                                            <a ka="search_150103" href="/c101210100-p150103/">HRBP</a>
                                                            <a ka="search_150104" href="/c101210100-p150104/">人力资源专员/助理</a>
                                                            <a ka="search_150105" href="/c101210100-p150105/">培训</a>
                                                            <a ka="search_150106" href="/c101210100-p150106/">薪资福利</a>
                                                            <a ka="search_150107" href="/c101210100-p150107/">绩效考核</a>
                                                            <a ka="search_150403" href="/c101210100-p150403/">人力资源经理</a>
                                                            <a ka="search_150406" href="/c101210100-p150406/">人力资源VP/CHO</a>
                                                            <a ka="search_150108" href="/c101210100-p150108/">人力资源总监</a>
                                                            <a ka="search_150109" href="/c101210100-p150109/">员工关系</a>
                                                            <a ka="search_150110" href="/c101210100-p150110/">组织发展</a>
                                                </div>
                                            </li>
                                            <li>
                                                <h4>行政</h4>
                                                <div class="text">
                                                            <a ka="search_150201" href="/c101210100-p150201/">行政专员/助理</a>
                                                            <a ka="search_150202" href="/c101210100-p150202/">前台</a>
                                                            <a ka="search_150204" href="/c101210100-p150204/">行政主管</a>
                                                            <a ka="search_150205" href="/c101210100-p150205/">经理助理</a>
                                                            <a ka="search_150207" href="/c101210100-p150207/">后勤</a>
                                                            <a ka="search_150208" href="/c101210100-p150208/">商务司机</a>
                                                            <a ka="search_150401" href="/c101210100-p150401/">行政经理</a>
                                                            <a ka="search_150209" href="/c101210100-p150209/">行政总监</a>
                                                </div>
                                            </li>
                                            <li>
                                                <h4>财务</h4>
                                                <div class="text">
                                                            <a ka="search_150399" href="/c101210100-p150399/">财务</a>
                                                            <a ka="search_150301" href="/c101210100-p150301/">会计</a>
                                                            <a ka="search_150302" href="/c101210100-p150302/">出纳</a>
                                                            <a ka="search_150303" href="/c101210100-p150303/">财务顾问</a>
                                                            <a ka="search_150304" href="/c101210100-p150304/">结算</a>
                                                            <a ka="search_150305" href="/c101210100-p150305/">税务</a>
                                                            <a ka="search_150306" href="/c101210100-p150306/">审计</a>
                                                            <a ka="search_150307" href="/c101210100-p150307/">风控</a>
                                                            <a ka="search_150402" href="/c101210100-p150402/">财务经理</a>
                                                            <a ka="search_150404" href="/c101210100-p150404/">CFO</a>
                                                            <a ka="search_150308" href="/c101210100-p150308/">财务总监</a>
                                                            <a ka="search_150309" href="/c101210100-p150309/">财务主管</a>
                                                </div>
                                            </li>
                                            <li>
                                                <h4>法务</h4>
                                                <div class="text">
                                                            <a ka="search_150203" href="/c101210100-p150203/">法务专员/助理</a>
                                                            <a ka="search_150502" href="/c101210100-p150502/">律师</a>
                                                            <a ka="search_150503" href="/c101210100-p150503/">专利</a>
                                                            <a ka="search_150504" href="/c101210100-p150504/">法律顾问</a>
                                                            <a ka="search_150505" href="/c101210100-p150505/">法务主管</a>
                                                            <a ka="search_150506" href="/c101210100-p150506/">法务经理</a>
                                                            <a ka="search_150507" href="/c101210100-p150507/">法务总监</a>
                                                </div>
                                            </li>
                                            <li>
                                                <h4>其他职能职位</h4>
                                                <div class="text">
                                                            <a ka="search_150601" href="/c101210100-p150601/">其他职能职位</a>
                                                </div>
                                            </li>
                                </ul>
                            </div>
                        </dl>
                        <dl class="">
                            <dd>
                                <i class="icon-arrow-right"></i>
                                <b>高级管理</b>
                                    <a href="/c101210100-p150407/">CEO/总裁/总经理</a>
                                    <a href="/c101210100-p150409/">事业部负责人</a>
                            </dd>
                            <div class="menu-line"></div>
                            <div class="menu-sub">
                                <p class="menu-article">高级管理</p>
                                <ul>
                                            <li>
                                                <h4>高级管理职位</h4>
                                                <div class="text">
                                                            <a ka="search_150499" href="/c101210100-p150499/">高级管理职位</a>
                                                            <a ka="search_150407" href="/c101210100-p150407/">CEO/总裁/总经理</a>
                                                            <a ka="search_150408" href="/c101210100-p150408/">副总裁/副总经理</a>
                                                            <a ka="search_150409" href="/c101210100-p150409/">事业部负责人</a>
                                                            <a ka="search_150410" href="/c101210100-p150410/">区域/分公司/代表处负责人</a>
                                                            <a ka="search_150411" href="/c101210100-p150411/">总裁/总经理/董事长助理</a>
                                                            <a ka="search_150412" href="/c101210100-p150412/">合伙人</a>
                                                            <a ka="search_150413" href="/c101210100-p150413/">创始人</a>
                                                            <a ka="search_150414" href="/c101210100-p150414/">董事会秘书</a>
                                                </div>
                                            </li>
                                </ul>
                            </div>
                        </dl>
                        <dl class="">
                            <dd>
                                <i class="icon-arrow-right"></i>
                                <b>销售</b>
                                    <a href="/c101210100-p140301/">销售专员</a>
                                    <a href="/c101210100-p140302/">销售经理</a>
                                    <a href="/c101210100-p140316/">销售工程师</a>
                            </dd>
                            <div class="menu-line"></div>
                            <div class="menu-sub">
                                <p class="menu-article">销售</p>
                                <ul>
                                            <li>
                                                <h4>销售</h4>
                                                <div class="text">
                                                            <a ka="search_140399" href="/c101210100-p140399/">销售</a>
                                                            <a ka="search_140301" href="/c101210100-p140301/">销售专员</a>
                                                            <a ka="search_140302" href="/c101210100-p140302/">销售经理</a>
                                                            <a ka="search_140303" href="/c101210100-p140303/">客户代表</a>
                                                            <a ka="search_140304" href="/c101210100-p140304/">大客户代表</a>
                                                            <a ka="search_140305" href="/c101210100-p140305/">BD经理</a>
                                                            <a ka="search_140306" href="/c101210100-p140306/">商务渠道</a>
                                                            <a ka="search_140307" href="/c101210100-p140307/">渠道销售</a>
                                                            <a ka="search_140308" href="/c101210100-p140308/">代理商销售</a>
                                                            <a ka="search_140309" href="/c101210100-p140309/">销售助理</a>
                                                            <a ka="search_140310" href="/c101210100-p140310/">电话销售</a>
                                                            <a ka="search_140311" href="/c101210100-p140311/">销售顾问</a>
                                                            <a ka="search_140312" href="/c101210100-p140312/">商品经理</a>
                                                            <a ka="search_140313" href="/c101210100-p140313/">广告销售</a>
                                                            <a ka="search_140314" href="/c101210100-p140314/">网络营销</a>
                                                            <a ka="search_140315" href="/c101210100-p140315/">营销主管</a>
                                                            <a ka="search_140316" href="/c101210100-p140316/">销售工程师</a>
                                                            <a ka="search_140317" href="/c101210100-p140317/">客户经理</a>
                                                </div>
                                            </li>
                                            <li>
                                                <h4>销售管理</h4>
                                                <div class="text">
                                                            <a ka="search_160199" href="/c101210100-p160199/">销售管理</a>
                                                            <a ka="search_140402" href="/c101210100-p140402/">销售总监</a>
                                                            <a ka="search_140403" href="/c101210100-p140403/">商务总监</a>
                                                            <a ka="search_160101" href="/c101210100-p160101/">区域总监</a>
                                                            <a ka="search_160102" href="/c101210100-p160102/">城市经理</a>
                                                            <a ka="search_160103" href="/c101210100-p160103/">销售VP</a>
                                                            <a ka="search_160104" href="/c101210100-p160104/">团队经理</a>
                                                </div>
                                            </li>
                                            <li>
                                                <h4>其他销售职位</h4>
                                                <div class="text">
                                                            <a ka="search_160201" href="/c101210100-p160201/">其他销售职位</a>
                                                </div>
                                            </li>
                                </ul>
                            </div>
                        </dl>
                        <dl class="">
                            <dd>
                                <i class="icon-arrow-right"></i>
                                <b>媒体</b>
                                    <a href="/c101210100-p170205/">文案</a>
                                    <a href="/c101210100-p170201/">广告创意</a>
                                    <a href="/c101210100-p170102/">编辑</a>
                                    <a href="/c101210100-p170101/">记者</a>
                                    <a href="/c101210100-p170301/">媒介经理</a>
                            </dd>
                            <div class="menu-line"></div>
                            <div class="menu-sub">
                                <p class="menu-article">媒体</p>
                                <ul>
                                            <li>
                                                <h4>采编/写作/出版</h4>
                                                <div class="text">
                                                            <a ka="search_170199" href="/c101210100-p170199/">采编/写作/出版</a>
                                                            <a ka="search_170101" href="/c101210100-p170101/">记者</a>
                                                            <a ka="search_170102" href="/c101210100-p170102/">编辑</a>
                                                            <a ka="search_170103" href="/c101210100-p170103/">采编</a>
                                                            <a ka="search_170104" href="/c101210100-p170104/">撰稿人</a>
                                                            <a ka="search_170105" href="/c101210100-p170105/">出版发行</a>
                                                            <a ka="search_170106" href="/c101210100-p170106/">校对录入</a>
                                                            <a ka="search_170107" href="/c101210100-p170107/">总编</a>
                                                            <a ka="search_170108" href="/c101210100-p170108/">自媒体</a>
                                                </div>
                                            </li>
                                            <li>
                                                <h4>公关媒介</h4>
                                                <div class="text">
                                                            <a ka="search_170399" href="/c101210100-p170399/">公关媒介</a>
                                                            <a ka="search_170301" href="/c101210100-p170301/">媒介经理</a>
                                                            <a ka="search_170302" href="/c101210100-p170302/">媒介专员</a>
                                                            <a ka="search_170303" href="/c101210100-p170303/">广告协调</a>
                                                            <a ka="search_170304" href="/c101210100-p170304/">品牌公关</a>
                                                            <a ka="search_170305" href="/c101210100-p170305/">活动策划执行</a>
                                                            <a ka="search_170306" href="/c101210100-p170306/">媒介策划</a>
                                                </div>
                                            </li>
                                            <li>
                                                <h4>会务会展</h4>
                                                <div class="text">
                                                            <a ka="search_170499" href="/c101210100-p170499/">会务会展</a>
                                                            <a ka="search_170401" href="/c101210100-p170401/">会议活动销售</a>
                                                            <a ka="search_170402" href="/c101210100-p170402/">会议活动策划</a>
                                                            <a ka="search_170403" href="/c101210100-p170403/">会议活动执行</a>
                                                            <a ka="search_170404" href="/c101210100-p170404/">会展活动销售</a>
                                                            <a ka="search_170405" href="/c101210100-p170405/">会展活动策划</a>
                                                            <a ka="search_170406" href="/c101210100-p170406/">会展活动执行</a>
                                                </div>
                                            </li>
                                            <li>
                                                <h4>广告</h4>
                                                <div class="text">
                                                            <a ka="search_170299" href="/c101210100-p170299/">广告</a>
                                                            <a ka="search_170201" href="/c101210100-p170201/">广告创意</a>
                                                            <a ka="search_170202" href="/c101210100-p170202/">美术指导</a>
                                                            <a ka="search_170203" href="/c101210100-p170203/">广告设计师</a>
                                                            <a ka="search_170204" href="/c101210100-p170204/">策划经理</a>
                                                            <a ka="search_170205" href="/c101210100-p170205/">文案</a>
                                                            <a ka="search_170207" href="/c101210100-p170207/">广告制作</a>
                                                            <a ka="search_170208" href="/c101210100-p170208/">媒介投放</a>
                                                            <a ka="search_170209" href="/c101210100-p170209/">媒介合作</a>
                                                            <a ka="search_170210" href="/c101210100-p170210/">媒介顾问</a>
                                                            <a ka="search_170211" href="/c101210100-p170211/">广告审核</a>
                                                </div>
                                            </li>
                                            <li>
                                                <h4>影视媒体</h4>
                                                <div class="text">
                                                            <a ka="search_170620" href="/c101210100-p170620/">主持人/DJ</a>
                                                            <a ka="search_170699" href="/c101210100-p170699/">影视媒体</a>
                                                            <a ka="search_170617" href="/c101210100-p170617/">助理</a>
                                                            <a ka="search_170618" href="/c101210100-p170618/">统筹制片人</a>
                                                            <a ka="search_170619" href="/c101210100-p170619/">执行制片人</a>
                                                            <a ka="search_170601" href="/c101210100-p170601/">导演/编导</a>
                                                            <a ka="search_170602" href="/c101210100-p170602/">摄影/摄像</a>
                                                            <a ka="search_170603" href="/c101210100-p170603/">视频编辑</a>
                                                            <a ka="search_170604" href="/c101210100-p170604/">音频编辑</a>
                                                            <a ka="search_170605" href="/c101210100-p170605/">经纪人</a>
                                                            <a ka="search_170606" href="/c101210100-p170606/">后期制作</a>
                                                            <a ka="search_170607" href="/c101210100-p170607/">影视制作</a>
                                                            <a ka="search_170608" href="/c101210100-p170608/">影视发行</a>
                                                            <a ka="search_170609" href="/c101210100-p170609/">影视策划</a>
                                                            <a ka="search_170610" href="/c101210100-p170610/">主播</a>
                                                            <a ka="search_170611" href="/c101210100-p170611/">演员/配音/模特</a>
                                                            <a ka="search_170612" href="/c101210100-p170612/">化妆/造型/服装</a>
                                                            <a ka="search_170613" href="/c101210100-p170613/">放映管理</a>
                                                            <a ka="search_170614" href="/c101210100-p170614/">录音/音效</a>
                                                            <a ka="search_170615" href="/c101210100-p170615/">制片人</a>
                                                            <a ka="search_170616" href="/c101210100-p170616/">编剧</a>
                                                </div>
                                            </li>
                                            <li>
                                                <h4>其他传媒职位</h4>
                                                <div class="text">
                                                            <a ka="search_170501" href="/c101210100-p170501/">其他传媒职位</a>
                                                </div>
                                            </li>
                                </ul>
                            </div>
                        </dl>
                        <dl class="">
                            <dd>
                                <i class="icon-arrow-right"></i>
                                <b>金融</b>
                                    <a href="/c101210100-p180101/">投资经理</a>
                                    <a href="/c101210100-p180112/">投资总监</a>
                                    <a href="/c101210100-p180201/">风控</a>
                                    <a href="/c101210100-p180899/">证券</a>
                            </dd>
                            <div class="menu-line"></div>
                            <div class="menu-sub">
                                <p class="menu-article">金融</p>
                                <ul>
                                            <li>
                                                <h4>投融资</h4>
                                                <div class="text">
                                                            <a ka="search_180199" href="/c101210100-p180199/">投融资</a>
                                                            <a ka="search_180101" href="/c101210100-p180101/">投资经理</a>
                                                            <a ka="search_180103" href="/c101210100-p180103/">行业研究</a>
                                                            <a ka="search_180104" href="/c101210100-p180104/">资产管理</a>
                                                            <a ka="search_180112" href="/c101210100-p180112/">投资总监</a>
                                                            <a ka="search_180113" href="/c101210100-p180113/">投资VP</a>
                                                            <a ka="search_180114" href="/c101210100-p180114/">投资合伙人</a>
                                                            <a ka="search_180115" href="/c101210100-p180115/">融资</a>
                                                            <a ka="search_180116" href="/c101210100-p180116/">并购</a>
                                                            <a ka="search_180117" href="/c101210100-p180117/">投后管理</a>
                                                            <a ka="search_180118" href="/c101210100-p180118/">投资助理</a>
                                                            <a ka="search_180111" href="/c101210100-p180111/">其他投融资职位</a>
                                                            <a ka="search_180119" href="/c101210100-p180119/">投资顾问</a>
                                                </div>
                                            </li>
                                            <li>
                                                <h4>风控</h4>
                                                <div class="text">
                                                            <a ka="search_180201" href="/c101210100-p180201/">风控</a>
                                                            <a ka="search_180202" href="/c101210100-p180202/">律师</a>
                                                            <a ka="search_180203" href="/c101210100-p180203/">资信评估</a>
                                                            <a ka="search_180204" href="/c101210100-p180204/">合规稽查</a>
                                                </div>
                                            </li>
                                            <li>
                                                <h4>税务审计</h4>
                                                <div class="text">
                                                            <a ka="search_180301" href="/c101210100-p180301/">审计</a>
                                                            <a ka="search_180302" href="/c101210100-p180302/">法务</a>
                                                            <a ka="search_180303" href="/c101210100-p180303/">会计</a>
                                                            <a ka="search_180304" href="/c101210100-p180304/">清算</a>
                                                </div>
                                            </li>
                                            <li>
                                                <h4>银行</h4>
                                                <div class="text">
                                                            <a ka="search_180499" href="/c101210100-p180499/">银行</a>
                                                            <a ka="search_180401" href="/c101210100-p180401/">信用卡销售</a>
                                                            <a ka="search_180102" href="/c101210100-p180102/">分析师</a>
                                                            <a ka="search_180402" href="/c101210100-p180402/">柜员</a>
                                                            <a ka="search_180403" href="/c101210100-p180403/">商务渠道</a>
                                                            <a ka="search_180404" href="/c101210100-p180404/">大堂经理</a>
                                                            <a ka="search_180105" href="/c101210100-p180105/">理财顾问</a>
                                                            <a ka="search_180405" href="/c101210100-p180405/">客户经理</a>
                                                            <a ka="search_180406" href="/c101210100-p180406/">信贷管理</a>
                                                            <a ka="search_180107" href="/c101210100-p180107/">风控</a>
                                                </div>
                                            </li>
                                            <li>
                                                <h4>互联网金融</h4>
                                                <div class="text">
                                                            <a ka="search_180599" href="/c101210100-p180599/">互联网金融</a>
                                                            <a ka="search_180501" href="/c101210100-p180501/">金融产品经理</a>
                                                            <a ka="search_180502" href="/c101210100-p180502/">风控</a>
                                                            <a ka="search_180503" href="/c101210100-p180503/">催收员</a>
                                                            <a ka="search_180504" href="/c101210100-p180504/">分析师</a>
                                                            <a ka="search_180505" href="/c101210100-p180505/">投资经理</a>
                                                            <a ka="search_180106" href="/c101210100-p180106/">交易员</a>
                                                            <a ka="search_180506" href="/c101210100-p180506/">理财顾问</a>
                                                            <a ka="search_180108" href="/c101210100-p180108/">合规稽查</a>
                                                            <a ka="search_180109" href="/c101210100-p180109/">审计</a>
                                                            <a ka="search_180110" href="/c101210100-p180110/">清算</a>
                                                </div>
                                            </li>
                                            <li>
                                                <h4>保险</h4>
                                                <div class="text">
                                                            <a ka="search_180701" href="/c101210100-p180701/">保险业务</a>
                                                            <a ka="search_180702" href="/c101210100-p180702/">精算师</a>
                                                            <a ka="search_180703" href="/c101210100-p180703/">保险理赔</a>
                                                </div>
                                            </li>
                                            <li>
                                                <h4>证券</h4>
                                                <div class="text">
                                                            <a ka="search_180899" href="/c101210100-p180899/">证券</a>
                                                            <a ka="search_180801" href="/c101210100-p180801/">证券经纪人</a>
                                                            <a ka="search_180802" href="/c101210100-p180802/">证券分析师</a>
                                                </div>
                                            </li>
                                            <li>
                                                <h4>其他金融职位</h4>
                                                <div class="text">
                                                            <a ka="search_180601" href="/c101210100-p180601/">其他金融职位</a>
                                                </div>
                                            </li>
                                </ul>
                            </div>
                        </dl>
                        <dl class="">
                            <dd>
                                <i class="icon-arrow-right"></i>
                                <b>汽车</b>
                                    <a href="/c101210100-p230201/">汽车销售</a>
                                    <a href="/c101210100-p230204/">汽车维修</a>
                                    <a href="/c101210100-p230107/">零部件设计</a>
                            </dd>
                            <div class="menu-line"></div>
                            <div class="menu-sub">
                                <p class="menu-article">汽车</p>
                                <ul>
                                            <li>
                                                <h4>汽车设计与研发</h4>
                                                <div class="text">
                                                            <a ka="search_230101" href="/c101210100-p230101/">汽车设计</a>
                                                            <a ka="search_230102" href="/c101210100-p230102/">车身设计</a>
                                                            <a ka="search_230103" href="/c101210100-p230103/">底盘设计</a>
                                                            <a ka="search_230104" href="/c101210100-p230104/">机械设计</a>
                                                            <a ka="search_230105" href="/c101210100-p230105/">动力系统设计</a>
                                                            <a ka="search_230106" href="/c101210100-p230106/">电子工程设计</a>
                                                            <a ka="search_230107" href="/c101210100-p230107/">零部件设计</a>
                                                            <a ka="search_230108" href="/c101210100-p230108/">汽车工程项目管理</a>
                                                            <a ka="search_230110" href="/c101210100-p230110/">内外饰设计工程师</a>
                                                </div>
                                            </li>
                                            <li>
                                                <h4>汽车生产与制造</h4>
                                                <div class="text">
                                                            <a ka="search_230210" href="/c101210100-p230210/">总装工程师</a>
                                                            <a ka="search_230211" href="/c101210100-p230211/">焊接工程师</a>
                                                            <a ka="search_230212" href="/c101210100-p230212/">冲压工程师</a>
                                                            <a ka="search_230109" href="/c101210100-p230109/">质量工程师</a>
                                                </div>
                                            </li>
                                            <li>
                                                <h4>汽车销售与服务</h4>
                                                <div class="text">
                                                            <a ka="search_230299" href="/c101210100-p230299/">汽车销售与制造</a>
                                                            <a ka="search_230201" href="/c101210100-p230201/">汽车销售</a>
                                                            <a ka="search_230202" href="/c101210100-p230202/">汽车配件销售</a>
                                                            <a ka="search_230203" href="/c101210100-p230203/">汽车售后服务</a>
                                                            <a ka="search_230204" href="/c101210100-p230204/">汽车维修</a>
                                                            <a ka="search_230205" href="/c101210100-p230205/">汽车美容</a>
                                                            <a ka="search_230206" href="/c101210100-p230206/">汽车定损理赔</a>
                                                            <a ka="search_230207" href="/c101210100-p230207/">二手车评估师</a>
                                                            <a ka="search_230208" href="/c101210100-p230208/">4S店管理</a>
                                                            <a ka="search_230209" href="/c101210100-p230209/">汽车改装工程师</a>
                                                </div>
                                            </li>
                                            <li>
                                                <h4>其他汽车职位</h4>
                                                <div class="text">
                                                            <a ka="search_230301" href="/c101210100-p230301/">其他汽车职位</a>
                                                </div>
                                            </li>
                                </ul>
                            </div>
                        </dl>
                        <dl class="">
                            <dd>
                                <i class="icon-arrow-right"></i>
                                <b>教育培训</b>
                                    <a href="/c101210100-p190101/">课程设计</a>
                                    <a href="/c101210100-p190202/">教务管理</a>
                                    <a href="/c101210100-p190499/">IT培训</a>
                            </dd>
                            <div class="menu-line"></div>
                            <div class="menu-sub">
                                <p class="menu-article">教育培训</p>
                                <ul>
                                            <li>
                                                <h4>教育产品研发</h4>
                                                <div class="text">
                                                            <a ka="search_190199" href="/c101210100-p190199/">教育产品研发</a>
                                                            <a ka="search_190101" href="/c101210100-p190101/">课程设计</a>
                                                            <a ka="search_190102" href="/c101210100-p190102/">课程编辑</a>
                                                            <a ka="search_190103" href="/c101210100-p190103/">教师</a>
                                                            <a ka="search_190104" href="/c101210100-p190104/">培训研究</a>
                                                            <a ka="search_190105" href="/c101210100-p190105/">培训师</a>
                                                            <a ka="search_190107" href="/c101210100-p190107/">培训策划</a>
                                                            <a ka="search_190106" href="/c101210100-p190106/">其他教育产品研发职位</a>
                                                </div>
                                            </li>
                                            <li>
                                                <h4>教育行政</h4>
                                                <div class="text">
                                                            <a ka="search_190299" href="/c101210100-p190299/">教育行政</a>
                                                            <a ka="search_190201" href="/c101210100-p190201/">校长</a>
                                                            <a ka="search_190202" href="/c101210100-p190202/">教务管理</a>
                                                            <a ka="search_190203" href="/c101210100-p190203/">教学管理</a>
                                                            <a ka="search_190204" href="/c101210100-p190204/">班主任/辅导员</a>
                                                </div>
                                            </li>
                                            <li>
                                                <h4>教师</h4>
                                                <div class="text">
                                                            <a ka="search_190301" href="/c101210100-p190301/">教师</a>
                                                            <a ka="search_190302" href="/c101210100-p190302/">助教</a>
                                                            <a ka="search_190303" href="/c101210100-p190303/">高中教师</a>
                                                            <a ka="search_190304" href="/c101210100-p190304/">初中教师</a>
                                                            <a ka="search_190305" href="/c101210100-p190305/">小学教师</a>
                                                            <a ka="search_190306" href="/c101210100-p190306/">幼教</a>
                                                            <a ka="search_190307" href="/c101210100-p190307/">理科教师</a>
                                                            <a ka="search_190308" href="/c101210100-p190308/">文科教师</a>
                                                            <a ka="search_190309" href="/c101210100-p190309/">外语教师</a>
                                                            <a ka="search_190310" href="/c101210100-p190310/">音乐教师</a>
                                                            <a ka="search_190311" href="/c101210100-p190311/">美术教师</a>
                                                            <a ka="search_190312" href="/c101210100-p190312/">体育教师</a>
                                                            <a ka="search_190313" href="/c101210100-p190313/">就业老师</a>
                                                </div>
                                            </li>
                                            <li>
                                                <h4>IT培训</h4>
                                                <div class="text">
                                                            <a ka="search_190499" href="/c101210100-p190499/">IT培训</a>
                                                            <a ka="search_190401" href="/c101210100-p190401/">JAVA培训讲师</a>
                                                            <a ka="search_190402" href="/c101210100-p190402/">Android培训讲师</a>
                                                            <a ka="search_190403" href="/c101210100-p190403/">ios培训讲师</a>
                                                            <a ka="search_190404" href="/c101210100-p190404/">PHP培训讲师</a>
                                                            <a ka="search_190405" href="/c101210100-p190405/">.NET培训讲师</a>
                                                            <a ka="search_190406" href="/c101210100-p190406/">C++培训讲师</a>
                                                            <a ka="search_190407" href="/c101210100-p190407/">Unity 3D培训讲师</a>
                                                            <a ka="search_190408" href="/c101210100-p190408/">Web前端培训讲师</a>
                                                            <a ka="search_190409" href="/c101210100-p190409/">软件测试培训讲师</a>
                                                            <a ka="search_190410" href="/c101210100-p190410/">动漫培训讲师</a>
                                                            <a ka="search_190411" href="/c101210100-p190411/">UI设计培训讲师</a>
                                                </div>
                                            </li>
                                            <li>
                                                <h4>职业培训</h4>
                                                <div class="text">
                                                            <a ka="search_190501" href="/c101210100-p190501/">财会培训讲师</a>
                                                            <a ka="search_190502" href="/c101210100-p190502/">HR培训讲师</a>
                                                            <a ka="search_190503" href="/c101210100-p190503/">培训师</a>
                                                            <a ka="search_190504" href="/c101210100-p190504/">拓展培训</a>
                                                </div>
                                            </li>
                                            <li>
                                                <h4>招生</h4>
                                                <div class="text">
                                                            <a ka="search_190601" href="/c101210100-p190601/">课程顾问</a>
                                                            <a ka="search_190602" href="/c101210100-p190602/">招生顾问</a>
                                                            <a ka="search_190603" href="/c101210100-p190603/">留学顾问</a>
                                                </div>
                                            </li>
                                            <li>
                                                <h4>教练</h4>
                                                <div class="text">
                                                            <a ka="search_190799" href="/c101210100-p190799/">教练</a>
                                                            <a ka="search_190701" href="/c101210100-p190701/">舞蹈教练</a>
                                                            <a ka="search_190702" href="/c101210100-p190702/">瑜伽教练</a>
                                                            <a ka="search_190703" href="/c101210100-p190703/">瘦身顾问</a>
                                                            <a ka="search_190704" href="/c101210100-p190704/">游泳教练</a>
                                                            <a ka="search_190705" href="/c101210100-p190705/">健身教练</a>
                                                            <a ka="search_190706" href="/c101210100-p190706/">篮球/羽毛球教练</a>
                                                            <a ka="search_190707" href="/c101210100-p190707/">跆拳道教练</a>
                                                </div>
                                            </li>
                                            <li>
                                                <h4>其他教育培训职位</h4>
                                                <div class="text">
                                                            <a ka="search_190801" href="/c101210100-p190801/">其他教育培训职位</a>
                                                </div>
                                            </li>
                                </ul>
                            </div>
                        </dl>
                    <div class="show-all">
                        显示全部职位
                    </div>

                    <div class="all-box">
                            <dl>
                                <dd>
                                    <i class="icon-arrow-right"></i>
                                    <b>医疗健康</b>
                                        <a href="/c101210100-p210104/">药剂师</a>
                                        <a href="/c101210100-p210401/">营养师</a>
                                        <a href="/c101210100-p210105/">医疗器械研究</a>
                                </dd>
                                <div class="menu-line"></div>
                                <div class="menu-sub">
                                    <p class="menu-article">医疗健康</p>
                                    <ul>
                                                <li>
                                                    <h4>医生/医技</h4>
                                                    <div class="text">
                                                                <a href="/c101210100-p210199/">医生/医技</a>
                                                                <a href="/c101210100-p210112/">医生助理</a>
                                                                <a href="/c101210100-p210113/">医学影像</a>
                                                                <a href="/c101210100-p210114/">B超医生</a>
                                                                <a href="/c101210100-p210302/">中医</a>
                                                                <a href="/c101210100-p210103/">医师</a>
                                                                <a href="/c101210100-p210303/">心理医生</a>
                                                                <a href="/c101210100-p210104/">药剂师</a>
                                                                <a href="/c101210100-p210304/">牙科医生</a>
                                                                <a href="/c101210100-p210305/">康复治疗师</a>
                                                                <a href="/c101210100-p210109/">验光师</a>
                                                                <a href="/c101210100-p210110/">放射科医师</a>
                                                                <a href="/c101210100-p210111/">检验科医师</a>
                                                                <a href="/c101210100-p210107/">其他医生职位</a>
                                                    </div>
                                                </li>
                                                <li>
                                                    <h4>护士/护理</h4>
                                                    <div class="text">
                                                                <a href="/c101210100-p210202/">护士长</a>
                                                                <a href="/c101210100-p210201/">护士/护理</a>
                                                                <a href="/c101210100-p210503/">导医</a>
                                                    </div>
                                                </li>
                                                <li>
                                                    <h4>健康整形</h4>
                                                    <div class="text">
                                                                <a href="/c101210100-p210499/">健康整形</a>
                                                                <a href="/c101210100-p210401/">营养师</a>
                                                                <a href="/c101210100-p210402/">整形师</a>
                                                                <a href="/c101210100-p210403/">理疗师</a>
                                                                <a href="/c101210100-p210404/">针灸推拿</a>
                                                    </div>
                                                </li>
                                                <li>
                                                    <h4>生物制药</h4>
                                                    <div class="text">
                                                                <a href="/c101210100-p210115/">生物制药</a>
                                                                <a href="/c101210100-p210116/">药品注册</a>
                                                                <a href="/c101210100-p210117/">药品生产</a>
                                                                <a href="/c101210100-p210118/">临床研究</a>
                                                                <a href="/c101210100-p210119/">临床协调</a>
                                                                <a href="/c101210100-p210120/">临床数据分析</a>
                                                                <a href="/c101210100-p210106/">医学总监</a>
                                                                <a href="/c101210100-p210108/">医药研发</a>
                                                    </div>
                                                </li>
                                                <li>
                                                    <h4>医疗器械</h4>
                                                    <div class="text">
                                                                <a href="/c101210100-p210121/">医疗器械注册</a>
                                                                <a href="/c101210100-p210122/">医疗器械生产/质量管理</a>
                                                                <a href="/c101210100-p210105/">医疗器械研究</a>
                                                    </div>
                                                </li>
                                                <li>
                                                    <h4>药店</h4>
                                                    <div class="text">
                                                                <a href="/c101210100-p210899/">药店</a>
                                                                <a href="/c101210100-p210801/">店长</a>
                                                                <a href="/c101210100-p210802/">执业药师/驻店药师</a>
                                                                <a href="/c101210100-p210803/">店员/营业员</a>
                                                    </div>
                                                </li>
                                                <li>
                                                    <h4>市场营销/媒体</h4>
                                                    <div class="text">
                                                                <a href="/c101210100-p210599/">市场营销/媒体</a>
                                                                <a href="/c101210100-p210506/">医疗器械销售</a>
                                                                <a href="/c101210100-p210101/">医学编辑</a>
                                                                <a href="/c101210100-p210501/">医学总监</a>
                                                                <a href="/c101210100-p210102/">药学编辑</a>
                                                                <a href="/c101210100-p210502/">医药代表</a>
                                                                <a href="/c101210100-p210504/">健康顾问</a>
                                                                <a href="/c101210100-p210505/">医美咨询</a>
                                                    </div>
                                                </li>
                                                <li>
                                                    <h4>其他医疗健康类职位</h4>
                                                    <div class="text">
                                                                <a href="/c101210100-p210701/">其他医疗健康类职位</a>
                                                    </div>
                                                </li>
                                    </ul>
                                </div>
                            </dl>
                            <dl>
                                <dd>
                                    <i class="icon-arrow-right"></i>
                                    <b>采购贸易</b>
                                        <a href="/c101210100-p250102/">采购经理</a>
                                        <a href="/c101210100-p250106/">采购主管</a>
                                        <a href="/c101210100-p250299/">进出口贸易</a>
                                </dd>
                                <div class="menu-line"></div>
                                <div class="menu-sub">
                                    <p class="menu-article">采购贸易</p>
                                    <ul>
                                                <li>
                                                    <h4>采购</h4>
                                                    <div class="text">
                                                                <a href="/c101210100-p250199/">采购</a>
                                                                <a href="/c101210100-p250101/">采购总监</a>
                                                                <a href="/c101210100-p250102/">采购经理</a>
                                                                <a href="/c101210100-p250103/">采购专员</a>
                                                                <a href="/c101210100-p250104/">买手</a>
                                                                <a href="/c101210100-p250105/">采购工程师</a>
                                                                <a href="/c101210100-p250106/">采购主管</a>
                                                                <a href="/c101210100-p250107/">采购助理</a>
                                                    </div>
                                                </li>
                                                <li>
                                                    <h4>进出口贸易</h4>
                                                    <div class="text">
                                                                <a href="/c101210100-p250299/">进出口贸易</a>
                                                                <a href="/c101210100-p250201/">外贸经理</a>
                                                                <a href="/c101210100-p250202/">外贸专员</a>
                                                                <a href="/c101210100-p250203/">外贸业务员</a>
                                                                <a href="/c101210100-p250204/">贸易跟单</a>
                                                    </div>
                                                </li>
                                                <li>
                                                    <h4>其他采购/贸易职位</h4>
                                                    <div class="text">
                                                                <a href="/c101210100-p250301/">其他采购/贸易类职位</a>
                                                    </div>
                                                </li>
                                    </ul>
                                </div>
                            </dl>
                            <dl>
                                <dd>
                                    <i class="icon-arrow-right"></i>
                                    <b>供应链/物流</b>
                                        <a href="/c101210100-p240103/">物流专员</a>
                                        <a href="/c101210100-p240107/">贸易跟单</a>
                                        <a href="/c101210100-p240102/">供应链经理</a>
                                </dd>
                                <div class="menu-line"></div>
                                <div class="menu-sub">
                                    <p class="menu-article">供应链/物流</p>
                                    <ul>
                                                <li>
                                                    <h4>物流</h4>
                                                    <div class="text">
                                                                <a href="/c101210100-p240199/">物流</a>
                                                                <a href="/c101210100-p240101/">供应链专员</a>
                                                                <a href="/c101210100-p240102/">供应链经理</a>
                                                                <a href="/c101210100-p240103/">物流专员</a>
                                                                <a href="/c101210100-p240104/">物流经理</a>
                                                                <a href="/c101210100-p240105/">物流运营</a>
                                                                <a href="/c101210100-p240106/">物流跟单</a>
                                                                <a href="/c101210100-p240107/">贸易跟单</a>
                                                                <a href="/c101210100-p240108/">物仓调度</a>
                                                                <a href="/c101210100-p240109/">物仓项目</a>
                                                                <a href="/c101210100-p240110/">运输经理/主管</a>
                                                                <a href="/c101210100-p240111/">货运代理专员</a>
                                                                <a href="/c101210100-p240112/">货运代理经理</a>
                                                                <a href="/c101210100-p240113/">水/空/陆运操作</a>
                                                                <a href="/c101210100-p240114/">报关员</a>
                                                                <a href="/c101210100-p240115/">报检员</a>
                                                                <a href="/c101210100-p240116/">核销员</a>
                                                                <a href="/c101210100-p240117/">单证员</a>
                                                    </div>
                                                </li>
                                                <li>
                                                    <h4>仓储</h4>
                                                    <div class="text">
                                                                <a href="/c101210100-p240299/">仓储</a>
                                                                <a href="/c101210100-p240201/">仓储物料经理</a>
                                                                <a href="/c101210100-p240202/">仓储物料专员</a>
                                                                <a href="/c101210100-p240203/">仓储物料项目</a>
                                                                <a href="/c101210100-p240204/">仓储管理</a>
                                                                <a href="/c101210100-p240205/">仓库文员</a>
                                                                <a href="/c101210100-p240206/">配/理/拣/发货</a>
                                                    </div>
                                                </li>
                                                <li>
                                                    <h4>运输</h4>
                                                    <div class="text">
                                                                <a href="/c101210100-p240399/">运输</a>
                                                                <a href="/c101210100-p240301/">货运司机</a>
                                                                <a href="/c101210100-p240302/">集装箱管理</a>
                                                                <a href="/c101210100-p240303/">配送</a>
                                                                <a href="/c101210100-p240304/">快递</a>
                                                    </div>
                                                </li>
                                                <li>
                                                    <h4>高端供应链职位</h4>
                                                    <div class="text">
                                                                <a href="/c101210100-p240499/">高端供应链职位</a>
                                                                <a href="/c101210100-p240401/">供应链总监</a>
                                                                <a href="/c101210100-p240402/">物流总监</a>
                                                    </div>
                                                </li>
                                                <li>
                                                    <h4>其他供应链职位</h4>
                                                    <div class="text">
                                                                <a href="/c101210100-p240501/">其他供应链职位</a>
                                                    </div>
                                                </li>
                                    </ul>
                                </div>
                            </dl>
                            <dl>
                                <dd>
                                    <i class="icon-arrow-right"></i>
                                    <b>房地产/建筑</b>
                                        <a href="/c101210100-p220401/">物业管理</a>
                                        <a href="/c101210100-p220199/">房地产规划开发</a>
                                </dd>
                                <div class="menu-line"></div>
                                <div class="menu-sub">
                                    <p class="menu-article">房地产/建筑</p>
                                    <ul>
                                                <li>
                                                    <h4>房地产规划开发</h4>
                                                    <div class="text">
                                                                <a href="/c101210100-p220199/">房地产规划开发</a>
                                                                <a href="/c101210100-p220101/">房产策划</a>
                                                                <a href="/c101210100-p220102/">地产项目管理</a>
                                                                <a href="/c101210100-p220103/">地产招投标</a>
                                                    </div>
                                                </li>
                                                <li>
                                                    <h4>设计装修与市政建设</h4>
                                                    <div class="text">
                                                                <a href="/c101210100-p220213/">弱电工程师</a>
                                                                <a href="/c101210100-p220299/">设计装修与市政建设</a>
                                                                <a href="/c101210100-p220201/">高级建筑工程师</a>
                                                                <a href="/c101210100-p220202/">建筑工程师</a>
                                                                <a href="/c101210100-p220203/">建筑设计师</a>
                                                                <a href="/c101210100-p220204/">土木/土建/结构工程师</a>
                                                                <a href="/c101210100-p220205/">室内设计</a>
                                                                <a href="/c101210100-p220206/">园林设计</a>
                                                                <a href="/c101210100-p220207/">城市规划设计</a>
                                                                <a href="/c101210100-p220208/">工程监理</a>
                                                                <a href="/c101210100-p220209/">工程造价</a>
                                                                <a href="/c101210100-p220210/">预结算</a>
                                                                <a href="/c101210100-p220211/">工程资料管理</a>
                                                                <a href="/c101210100-p220212/">建筑施工现场管理</a>
                                                    </div>
                                                </li>
                                                <li>
                                                    <h4>房地产经纪</h4>
                                                    <div class="text">
                                                                <a href="/c101210100-p220399/">房地产经纪</a>
                                                                <a href="/c101210100-p220301/">地产置业顾问</a>
                                                                <a href="/c101210100-p220302/">地产评估</a>
                                                                <a href="/c101210100-p220303/">地产中介</a>
                                                    </div>
                                                </li>
                                                <li>
                                                    <h4>物业管理</h4>
                                                    <div class="text">
                                                                <a href="/c101210100-p220401/">物业管理</a>
                                                                <a href="/c101210100-p220402/">物业租赁销售 </a>
                                                                <a href="/c101210100-p220403/">物业招商管理</a>
                                                    </div>
                                                </li>
                                                <li>
                                                    <h4>高端房地产职位</h4>
                                                    <div class="text">
                                                                <a href="/c101210100-p220599/">高端房地产职位</a>
                                                                <a href="/c101210100-p220501/">地产项目总监</a>
                                                                <a href="/c101210100-p220502/">地产策划总监</a>
                                                                <a href="/c101210100-p220503/">地产招投标总监</a>
                                                                <a href="/c101210100-p220504/">物业总监</a>
                                                                <a href="/c101210100-p220505/">房地产销售总监</a>
                                                    </div>
                                                </li>
                                                <li>
                                                    <h4>其他房地产职位</h4>
                                                    <div class="text">
                                                                <a href="/c101210100-p220601/">其他房地产职位</a>
                                                    </div>
                                                </li>
                                    </ul>
                                </div>
                            </dl>
                            <dl>
                                <dd>
                                    <i class="icon-arrow-right"></i>
                                    <b>咨询/翻译/法律</b>
                                        <a href="/c101210100-p260101/">企业管理咨询</a>
                                        <a href="/c101210100-p260201/">事务所律师</a>
                                </dd>
                                <div class="menu-line"></div>
                                <div class="menu-sub">
                                    <p class="menu-article">咨询/翻译/法律</p>
                                    <ul>
                                                <li>
                                                    <h4>咨询/调研</h4>
                                                    <div class="text">
                                                                <a href="/c101210100-p260199/">咨询/调研</a>
                                                                <a href="/c101210100-p260101/">企业管理咨询</a>
                                                                <a href="/c101210100-p260102/">数据分析师</a>
                                                                <a href="/c101210100-p260103/">财务咨询顾问</a>
                                                                <a href="/c101210100-p260104/">IT咨询顾问</a>
                                                                <a href="/c101210100-p260105/">人力资源顾问</a>
                                                                <a href="/c101210100-p260106/">咨询项目管理</a>
                                                                <a href="/c101210100-p260107/">战略咨询</a>
                                                                <a href="/c101210100-p260108/">猎头顾问</a>
                                                                <a href="/c101210100-p260109/">市场调研</a>
                                                                <a href="/c101210100-p260110/">其他咨询顾问</a>
                                                    </div>
                                                </li>
                                                <li>
                                                    <h4>律师</h4>
                                                    <div class="text">
                                                                <a href="/c101210100-p260203/">知识产权</a>
                                                                <a href="/c101210100-p260201/">事务所律师</a>
                                                                <a href="/c101210100-p260202/">公司法务</a>
                                                    </div>
                                                </li>
                                                <li>
                                                    <h4>翻译</h4>
                                                    <div class="text">
                                                                <a href="/c101210100-p260301/">英语翻译</a>
                                                                <a href="/c101210100-p260302/">日语翻译</a>
                                                                <a href="/c101210100-p260303/">韩语/朝鲜语翻译</a>
                                                                <a href="/c101210100-p260304/">法语翻译</a>
                                                                <a href="/c101210100-p260305/">德语翻译</a>
                                                                <a href="/c101210100-p260306/">俄语翻译</a>
                                                                <a href="/c101210100-p260307/">西班牙语翻译</a>
                                                                <a href="/c101210100-p260308/">其他语种翻译</a>
                                                    </div>
                                                </li>
                                                <li>
                                                    <h4>高端咨询类职位</h4>
                                                    <div class="text">
                                                                <a href="/c101210100-p260499/">高端咨询类职位</a>
                                                                <a href="/c101210100-p260401/">咨询总监</a>
                                                                <a href="/c101210100-p260402/">咨询经理</a>
                                                                <a href="/c101210100-p260403/">高级翻译</a>
                                                                <a href="/c101210100-p260404/">同声传译  </a>
                                                    </div>
                                                </li>
                                                <li>
                                                    <h4>其他咨询类职位</h4>
                                                    <div class="text">
                                                                <a href="/c101210100-p260501/">其他咨询/翻译类职位</a>
                                                    </div>
                                                </li>
                                    </ul>
                                </div>
                            </dl>
                            <dl>
                                <dd>
                                    <i class="icon-arrow-right"></i>
                                    <b>实习生/管培生</b>
                                        <a href="/c101210100-p270101/">实习生</a>
                                        <a href="/c101210100-p270102/">管培生</a>
                                        <a href="/c101210100-p270103/">储备干部</a>
                                </dd>
                                <div class="menu-line"></div>
                                <div class="menu-sub">
                                    <p class="menu-article">实习生/管培生</p>
                                    <ul>
                                                <li>
                                                    <h4>管培生/储备干部</h4>
                                                    <div class="text">
                                                                <a href="/c101210100-p270102/">管理培训生</a>
                                                                <a href="/c101210100-p270103/">储备干部</a>
                                                    </div>
                                                </li>
                                                <li>
                                                    <h4>其他管培生职位</h4>
                                                    <div class="text">
                                                                <a href="/c101210100-p270201/">其他实习/培训/储备职位</a>
                                                    </div>
                                                </li>
                                    </ul>
                                </div>
                            </dl>
                            <dl>
                                <dd>
                                    <i class="icon-arrow-right"></i>
                                    <b>旅游</b>
                                        <a href="/c101210100-p280103/">旅游顾问</a>
                                        <a href="/c101210100-p280104/">导游</a>
                                        <a href="/c101210100-p280299/">旅游产品开发/策划</a>
                                </dd>
                                <div class="menu-line"></div>
                                <div class="menu-sub">
                                    <p class="menu-article">旅游</p>
                                    <ul>
                                                <li>
                                                    <h4>旅游服务</h4>
                                                    <div class="text">
                                                                <a href="/c101210100-p280199/">旅游服务</a>
                                                                <a href="/c101210100-p280101/">计调</a>
                                                                <a href="/c101210100-p280102/">签证</a>
                                                                <a href="/c101210100-p280103/">旅游顾问</a>
                                                                <a href="/c101210100-p280104/">导游</a>
                                                                <a href="/c101210100-p280105/">预定票务</a>
                                                    </div>
                                                </li>
                                                <li>
                                                    <h4>旅游产品开发/策划</h4>
                                                    <div class="text">
                                                                <a href="/c101210100-p280299/">旅游产品开发/策划</a>
                                                                <a href="/c101210100-p280201/">旅游产品经理</a>
                                                                <a href="/c101210100-p280202/">旅游策划师</a>
                                                    </div>
                                                </li>
                                                <li>
                                                    <h4>其他旅游职位</h4>
                                                    <div class="text">
                                                                <a href="/c101210100-p280301/">其他旅游职位</a>
                                                    </div>
                                                </li>
                                    </ul>
                                </div>
                            </dl>
                            <dl>
                                <dd>
                                    <i class="icon-arrow-right"></i>
                                    <b>服务业</b>
                                        <a href="/c101210100-p290202/">酒店前台</a>
                                        <a href="/c101210100-p290103/">客房服务员</a>
                                        <a href="/c101210100-p210607/">发型师</a>
                                </dd>
                                <div class="menu-line"></div>
                                <div class="menu-sub">
                                    <p class="menu-article">服务业</p>
                                    <ul>
                                                <li>
                                                    <h4>安保/家政</h4>
                                                    <div class="text">
                                                                <a href="/c101210100-p290105/">保安</a>
                                                                <a href="/c101210100-p290106/">保洁</a>
                                                    </div>
                                                </li>
                                                <li>
                                                    <h4>婚礼/花艺</h4>
                                                    <div class="text">
                                                                <a href="/c101210100-p290701/">花艺师</a>
                                                                <a href="/c101210100-p290702/">婚礼策划师</a>
                                                    </div>
                                                </li>
                                                <li>
                                                    <h4>酒店</h4>
                                                    <div class="text">
                                                                <a href="/c101210100-p290107/">礼仪迎宾</a>
                                                                <a href="/c101210100-p290199/">酒店</a>
                                                                <a href="/c101210100-p290101/">收银</a>
                                                                <a href="/c101210100-p290102/">酒店前台</a>
                                                                <a href="/c101210100-p290103/">客房服务员</a>
                                                                <a href="/c101210100-p290104/">酒店经理</a>
                                                    </div>
                                                </li>
                                                <li>
                                                    <h4>餐饮</h4>
                                                    <div class="text">
                                                                <a href="/c101210100-p290208/">后厨</a>
                                                                <a href="/c101210100-p290209/">配菜打荷</a>
                                                                <a href="/c101210100-p290210/">茶艺师</a>
                                                                <a href="/c101210100-p290211/">西点师</a>
                                                                <a href="/c101210100-p290212/">餐饮学徒</a>
                                                                <a href="/c101210100-p290299/">餐饮</a>
                                                                <a href="/c101210100-p290201/">收银</a>
                                                                <a href="/c101210100-p290202/">服务员</a>
                                                                <a href="/c101210100-p290203/">厨师</a>
                                                                <a href="/c101210100-p290204/">咖啡师</a>
                                                                <a href="/c101210100-p290205/">送餐员</a>
                                                                <a href="/c101210100-p290206/">餐饮店长</a>
                                                                <a href="/c101210100-p290207/">领班</a>
                                                    </div>
                                                </li>
                                                <li>
                                                    <h4>零售</h4>
                                                    <div class="text">
                                                                <a href="/c101210100-p290305/">督导/巡店</a>
                                                                <a href="/c101210100-p290306/">陈列员</a>
                                                                <a href="/c101210100-p290307/">理货员</a>
                                                                <a href="/c101210100-p290399/">零售</a>
                                                                <a href="/c101210100-p290301/">收银</a>
                                                                <a href="/c101210100-p290302/">导购</a>
                                                                <a href="/c101210100-p290303/">店员/营业员</a>
                                                                <a href="/c101210100-p290304/">门店店长</a>
                                                    </div>
                                                </li>
                                                <li>
                                                    <h4>美容/健身</h4>
                                                    <div class="text">
                                                                <a href="/c101210100-p210607/">发型师</a>
                                                                <a href="/c101210100-p210608/">美甲师</a>
                                                                <a href="/c101210100-p210609/">化妆师</a>
                                                                <a href="/c101210100-p210610/">会籍顾问</a>
                                                                <a href="/c101210100-p210699/">健身</a>
                                                                <a href="/c101210100-p210601/">瑜伽教练</a>
                                                                <a href="/c101210100-p210602/">瘦身顾问</a>
                                                                <a href="/c101210100-p210603/">游泳教练</a>
                                                                <a href="/c101210100-p210604/">美体教练</a>
                                                                <a href="/c101210100-p210405/">美容师/顾问</a>
                                                                <a href="/c101210100-p210605/">舞蹈教练</a>
                                                                <a href="/c101210100-p210606/">健身教练</a>
                                                    </div>
                                                </li>
                                                <li>
                                                    <h4>其他服务业职位</h4>
                                                    <div class="text">
                                                                <a href="/c101210100-p290401/">其他服务业职位</a>
                                                    </div>
                                                </li>
                                    </ul>
                                </div>
                            </dl>
                            <dl>
                                <dd>
                                    <i class="icon-arrow-right"></i>
                                    <b>生产制造</b>
                                        <a href="/c101210100-p300102/">生产总监</a>
                                        <a href="/c101210100-p300105/">安全员</a>
                                        <a href="/c101210100-p300201/">质量管理/测试</a>
                                </dd>
                                <div class="menu-line"></div>
                                <div class="menu-sub">
                                    <p class="menu-article">生产制造</p>
                                    <ul>
                                                <li>
                                                    <h4>生产营运</h4>
                                                    <div class="text">
                                                                <a href="/c101210100-p300199/">生产营运</a>
                                                                <a href="/c101210100-p300101/">厂长/工厂经理</a>
                                                                <a href="/c101210100-p300102/">生产总监</a>
                                                                <a href="/c101210100-p300103/">生产经理/车间主任</a>
                                                                <a href="/c101210100-p300104/">生产组长/拉长</a>
                                                                <a href="/c101210100-p300105/">生产员</a>
                                                                <a href="/c101210100-p300106/">生产设备管理</a>
                                                                <a href="/c101210100-p300107/">生产计划/物料控制</a>
                                                                <a href="/c101210100-p300108/">生产跟单</a>
                                                    </div>
                                                </li>
                                                <li>
                                                    <h4>质量安全</h4>
                                                    <div class="text">
                                                                <a href="/c101210100-p300208/">质检员</a>
                                                                <a href="/c101210100-p300201/">质量管理/测试</a>
                                                                <a href="/c101210100-p300202/">可靠度工程师</a>
                                                                <a href="/c101210100-p300203/">故障分析师</a>
                                                                <a href="/c101210100-p300204/">认证工程师</a>
                                                                <a href="/c101210100-p300205/">体系工程师</a>
                                                                <a href="/c101210100-p300206/">审核员</a>
                                                                <a href="/c101210100-p300207/">安全员</a>
                                                    </div>
                                                </li>
                                                <li>
                                                    <h4>机械设计/制造</h4>
                                                    <div class="text">
                                                                <a href="/c101210100-p300399/">机械设计/制造</a>
                                                                <a href="/c101210100-p300301/">机械工程师</a>
                                                                <a href="/c101210100-p300302/">机械设计师</a>
                                                                <a href="/c101210100-p300303/">机械设备工程师</a>
                                                                <a href="/c101210100-p300304/">机械维修/保养</a>
                                                                <a href="/c101210100-p300305/">机械制图</a>
                                                                <a href="/c101210100-p300306/">机械结构工程师</a>
                                                                <a href="/c101210100-p300307/">工业工程师</a>
                                                                <a href="/c101210100-p300308/">工艺/制程工程师</a>
                                                                <a href="/c101210100-p300309/">材料工程师</a>
                                                                <a href="/c101210100-p300310/">机电工程师</a>
                                                                <a href="/c101210100-p300311/">CNC/数控</a>
                                                                <a href="/c101210100-p300312/">冲压工程师</a>
                                                                <a href="/c101210100-p300313/">夹具工程师</a>
                                                                <a href="/c101210100-p300314/">模具工程师</a>
                                                                <a href="/c101210100-p300315/">焊接工程师</a>
                                                                <a href="/c101210100-p300316/">注塑工程师</a>
                                                                <a href="/c101210100-p300317/">铸造/锻造工程师</a>
                                                    </div>
                                                </li>
                                                <li>
                                                    <h4>化工</h4>
                                                    <div class="text">
                                                                <a href="/c101210100-p300499/">化工</a>
                                                                <a href="/c101210100-p300401/">化工工程师</a>
                                                                <a href="/c101210100-p300402/">实验室技术员</a>
                                                                <a href="/c101210100-p300403/">化学分析</a>
                                                                <a href="/c101210100-p300404/">涂料研发</a>
                                                                <a href="/c101210100-p300405/">化妆品研发</a>
                                                                <a href="/c101210100-p300406/">食品/饮料研发</a>
                                                    </div>
                                                </li>
                                                <li>
                                                    <h4>服装/纺织/皮革</h4>
                                                    <div class="text">
                                                                <a href="/c101210100-p300501/">服装设计</a>
                                                                <a href="/c101210100-p300502/">女装设计</a>
                                                                <a href="/c101210100-p300503/">男装设计</a>
                                                                <a href="/c101210100-p300504/">童装设计</a>
                                                                <a href="/c101210100-p300505/">内衣设计</a>
                                                                <a href="/c101210100-p300506/">面料设计</a>
                                                                <a href="/c101210100-p300507/">面料辅料开发</a>
                                                                <a href="/c101210100-p300508/">面料辅料采购</a>
                                                                <a href="/c101210100-p300509/">打样/制版</a>
                                                                <a href="/c101210100-p300510/">服装/纺织/皮革跟单</a>
                                                    </div>
                                                </li>
                                                <li>
                                                    <h4>技工/普工</h4>
                                                    <div class="text">
                                                                <a href="/c101210100-p300601/">普工/操作工</a>
                                                                <a href="/c101210100-p300602/">叉车</a>
                                                                <a href="/c101210100-p300603/">铲车</a>
                                                                <a href="/c101210100-p300604/">焊工</a>
                                                                <a href="/c101210100-p300605/">氩弧焊工</a>
                                                                <a href="/c101210100-p300606/">电工</a>
                                                                <a href="/c101210100-p300608/">木工</a>
                                                                <a href="/c101210100-p300609/">漆工</a>
                                                                <a href="/c101210100-p300610/">车工</a>
                                                                <a href="/c101210100-p300611/">磨工</a>
                                                                <a href="/c101210100-p300612/">铣工</a>
                                                                <a href="/c101210100-p300613/">钳工</a>
                                                                <a href="/c101210100-p300614/">钻工</a>
                                                                <a href="/c101210100-p300615/">铆工</a>
                                                                <a href="/c101210100-p300616/">钣金</a>
                                                                <a href="/c101210100-p300617/">抛光</a>
                                                                <a href="/c101210100-p300618/">机修工</a>
                                                                <a href="/c101210100-p300619/">折弯工</a>
                                                                <a href="/c101210100-p300620/">电镀工</a>
                                                                <a href="/c101210100-p300621/">喷塑工</a>
                                                                <a href="/c101210100-p300622/">注塑工</a>
                                                                <a href="/c101210100-p300623/">组装工</a>
                                                                <a href="/c101210100-p300624/">包装工</a>
                                                                <a href="/c101210100-p300625/">空调工</a>
                                                                <a href="/c101210100-p300626/">电梯工</a>
                                                                <a href="/c101210100-p300627/">锅炉工</a>
                                                                <a href="/c101210100-p300628/">学徒工</a>
                                                    </div>
                                                </li>
                                                <li>
                                                    <h4>其他生产制造职位</h4>
                                                    <div class="text">
                                                                <a href="/c101210100-p300701/">其他生产制造职位</a>
                                                    </div>
                                                </li>
                                    </ul>
                                </div>
                            </dl>
                    </div>
                </div>
                <!--<div class="promotion-img"><a href="#"><img src="http://172.16.0.44/v2/web/geek/images/promotion-1.png" alt="" /></a></div>-->
            </div>
            <div class="home-main">
                <div class="slider-box">
                    <div class="promotion-main">
"""
def parse_text():

    html = etree.HTML(text)

    print(etree.tostring(html,encoding="utf-8").decode('utf-8'))

def parse_file():
    html = etree.parse("test.html")
    print(etree.tostring(html, encoding="utf-8").decode('utf-8'))


if __name__ == '__main__':
    parse_file()
