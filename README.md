# milk
###########环境依赖：
安装requirements.txt中所有包

###########运行步骤：
在该文件夹中创建虚拟环境并激活：
python –m venv djldjango
djldjango\Scripts\activate

###########目录结构描述：
milk:.
│  manage.py   //Django的任务管理命令行工具
│  readme.txt
│  requirements.txt
│  
├─.idea
│  │  .gitignore
│  │  dbnavigator.xml
│  │  deployment.xml
│  │  milk.iml
│  │  misc.xml
│  │  modules.xml
│  │  sshConfigs.xml
│  │  vcs.xml
│  │  webServers.xml
│  │  workspace.xml
│  │  
│  └─inspectionProfiles
│          profiles_settings.xml
│          
├─calorie   //实现计算卡路里的功能
│  │  admin.py
│  │  apps.py
│  │  models.py
│  │  readme.txt
│  │  tests.py
│  │  urls.py
│  │  views.py
│  │  __init__.py
│  │  
│  ├─migrations
│  │  │  __init__.py
│  │  │  
│  │  └─__pycache__
│  │          __init__.cpython-38.pyc
│  │          
│  └─__pycache__
│          admin.cpython-38.pyc
│          apps.cpython-38.pyc
│          models.cpython-38.pyc
│          urls.cpython-38.pyc
│          views.cpython-38.pyc
│          __init__.cpython-38.pyc
│          
├─carbon   //实现计算碳水化合物的功能
│  │  admin.py
│  │  apps.py
│  │  models.py
│  │  readme.txt
│  │  tests.py
│  │  urls.py
│  │  views.py
│  │  __init__.py
│  │  
│  ├─migrations
│  │  │  __init__.py
│  │  │  
│  │  └─__pycache__
│  │          __init__.cpython-38.pyc
│  │          
│  └─__pycache__
│          admin.cpython-38.pyc
│          apps.cpython-38.pyc
│          models.cpython-38.pyc
│          urls.cpython-38.pyc
│          views.cpython-38.pyc
│          __init__.cpython-38.pyc
│          
├─circle  //实现奶茶圈的功能
│  │  admin.py
│  │  apps.py
│  │  models.py
│  │  readme.txt
│  │  tests.py
│  │  urls.py
│  │  views.py
│  │  __init__.py
│  │  
│  ├─migrations
│  │  │  0001_initial.py
│  │  │  0002_circle_like.py
│  │  │  __init__.py
│  │  │  
│  │  └─__pycache__
│  │          0001_initial.cpython-38.pyc
│  │          0002_circle_like(1).cpython-38.pyc
│  │          0002_circle_like.cpython-38.pyc
│  │          __init__.cpython-38.pyc
│  │          
│  └─__pycache__
│          admin.cpython-38.pyc
│          apps.cpython-38.pyc
│          models.cpython-38.pyc
│          urls.cpython-38.pyc
│          views.cpython-38.pyc
│          __init__.cpython-38.pyc
│          
├─decision   //实现帮助店家决策的功能
│  │  admin.py
│  │  apps.py
│  │  models.py
│  │  readme.txt
│  │  tests.py
│  │  urls.py
│  │  views.py
│  │  __init__.py
│  │  
│  ├─.idea
│  │  │  .gitignore
│  │  │  .name
│  │  │  decision_tree.iml
│  │  │  misc.xml
│  │  │  modules.xml
│  │  │  workspace.xml
│  │  │  
│  │  └─inspectionProfiles
│  │          profiles_settings.xml
│  │          Project_Default.xml
│  │          
│  ├─migrations
│  │  │  __init__.py
│  │  │  
│  │  └─__pycache__
│  │          __init__.cpython-38.pyc
│  │          
│  └─__pycache__
│          admin.cpython-38.pyc
│          apps.cpython-38.pyc
│          models.cpython-38.pyc
│          urls.cpython-38.pyc
│          views.cpython-38.pyc
│          __init__.cpython-38.pyc
│          
├─indentify   //实现识别小料的功能
│  │  admin.py
│  │  apps.py
│  │  models.py  
│  │  readme.txt
│  │  tests.py
│  │  urls.py
│  │  views.py
│  │  __init__.py
│  │  
│  ├─migrations
│  │  │  grey1.png
│  │  │  __init__.py
│  │  │  
│  │  └─__pycache__
│  │          __init__.cpython-38.pyc
│  │          
│  └─__pycache__
│          admin.cpython-38.pyc
│          apps.cpython-38.pyc
│          models.cpython-38.pyc
│          urls.cpython-38.pyc
│          views.cpython-38.pyc
│          __init__.cpython-38.pyc
│          
├─milk  //主文件
│  │  asgi.py
│  │  readme.txt
│  │  settings.py  //包括了项目的初始化设置，可以针对整个项目进行有关参数配置，比如配置数据库、添加应用等。
│  │  urls.py   //用来声明并调用在views.py中的新建的方法。
│  │  view.py  //用户保存响应各种请求的函数或者类。创建一个可供页面调用并返回数据的方法，使用HTTPResponse返回页面所需数据。
│  │  wsgi.py   //wsgi.py定义所创建的项目都是WSGI应用。
│  │  __init__.py
│  │  
│  └─__pycache__
│          settings.cpython-38.pyc
│          urls.cpython-38.pyc
│          view.cpython-38.pyc
│          wsgi.cpython-38.pyc
│          __init__.cpython-38.pyc
│          
├─protein  //实现计算蛋白质的功能
│  │  admin.py
│  │  apps.py
│  │  models.py
│  │  readme.txt
│  │  tests.py
│  │  urls.py
│  │  views.py
│  │  __init__.py
│  │  
│  ├─migrations
│  │  │  __init__.py
│  │  │  
│  │  └─__pycache__
│  │          __init__.cpython-38.pyc
│  │          
│  └─__pycache__
│          admin.cpython-38.pyc
│          apps.cpython-38.pyc
│          models.cpython-38.pyc
│          urls.cpython-38.pyc
│          views.cpython-38.pyc
│          __init__.cpython-38.pyc
│          
├─static   //所有静态文件，包括图片，前端样式，字体
│  │  circle.css
│  │  game.css
│  │  indentify.css
│  │  load.css
│  │  main.css
│  │  readme.txt
│  │  
│  ├─admin
│  │  ├─css
│  │  │  │  autocomplete.css
│  │  │  │  base.css
│  │  │  │  changelists.css
│  │  │  │  dashboard.css
│  │  │  │  fonts.css
│  │  │  │  forms.css
│  │  │  │  login.css
│  │  │  │  responsive.css
│  │  │  │  responsive_rtl.css
│  │  │  │  rtl.css
│  │  │  │  widgets.css
│  │  │  │  
│  │  │  └─vendor
│  │  │      └─select2
│  │  │              LICENSE-SELECT2.md
│  │  │              select2.css
│  │  │              select2.min.css
│  │  │              
│  │  ├─fonts
│  │  │      LICENSE.txt
│  │  │      README.txt
│  │  │      Roboto-Bold-webfont.woff
│  │  │      Roboto-Light-webfont.woff
│  │  │      Roboto-Regular-webfont.woff
│  │  │      
│  │  ├─img
│  │  │  │  calendar-icons.svg
│  │  │  │  icon-addlink.svg
│  │  │  │  icon-alert.svg
│  │  │  │  icon-calendar.svg
│  │  │  │  icon-changelink.svg
│  │  │  │  icon-clock.svg
│  │  │  │  icon-deletelink.svg
│  │  │  │  icon-no.svg
│  │  │  │  icon-unknown-alt.svg
│  │  │  │  icon-unknown.svg
│  │  │  │  icon-viewlink.svg
│  │  │  │  icon-yes.svg
│  │  │  │  inline-delete.svg
│  │  │  │  LICENSE
│  │  │  │  README.txt
│  │  │  │  search.svg
│  │  │  │  selector-icons.svg
│  │  │  │  sorting-icons.svg
│  │  │  │  tooltag-add.svg
│  │  │  │  tooltag-arrowright.svg
│  │  │  │  
│  │  │  └─gis
│  │  │          move_vertex_off.svg
│  │  │          move_vertex_on.svg
│  │  │          
│  │  └─js
│  │      │  actions.js
│  │      │  actions.min.js
│  │      │  autocomplete.js
│  │      │  calendar.js
│  │      │  cancel.js
│  │      │  change_form.js
│  │      │  collapse.js
│  │      │  collapse.min.js
│  │      │  core.js
│  │      │  inlines.js
│  │      │  inlines.min.js
│  │      │  jquery.init.js
│  │      │  popup_response.js
│  │      │  prepopulate.js
│  │      │  prepopulate.min.js
│  │      │  prepopulate_init.js
│  │      │  SelectBox.js
│  │      │  SelectFilter2.js
│  │      │  timeparse.js
│  │      │  urlify.js
│  │      │  
│  │      ├─admin
│  │      │      DateTimeShortcuts.js
│  │      │      RelatedObjectLookups.js
│  │      │      
│  │      └─vendor
│  │          ├─jquery
│  │          │      jquery.js
│  │          │      jquery.min.js
│  │          │      LICENSE.txt
│  │          │      
│  │          ├─select2
│  │          │  │  LICENSE.md
│  │          │  │  select2.full.js
│  │          │  │  select2.full.min.js
│  │          │  │  
│  │          │  └─i18n
│  │          │          ar.js
│  │          │          az.js
│  │          │          bg.js
│  │          │          ca.js
│  │          │          cs.js
│  │          │          da.js
│  │          │          de.js
│  │          │          el.js
│  │          │          en.js
│  │          │          es.js
│  │          │          et.js
│  │          │          eu.js
│  │          │          fa.js
│  │          │          fi.js
│  │          │          fr.js
│  │          │          gl.js
│  │          │          he.js
│  │          │          hi.js
│  │          │          hr.js
│  │          │          hu.js
│  │          │          id.js
│  │          │          is.js
│  │          │          it.js
│  │          │          ja.js
│  │          │          km.js
│  │          │          ko.js
│  │          │          lt.js
│  │          │          lv.js
│  │          │          mk.js
│  │          │          ms.js
│  │          │          nb.js
│  │          │          nl.js
│  │          │          pl.js
│  │          │          pt-BR.js
│  │          │          pt.js
│  │          │          ro.js
│  │          │          ru.js
│  │          │          sk.js
│  │          │          sr-Cyrl.js
│  │          │          sr.js
│  │          │          sv.js
│  │          │          th.js
│  │          │          tr.js
│  │          │          uk.js
│  │          │          vi.js
│  │          │          zh-CN.js
│  │          │          zh-TW.js
│  │          │          
│  │          └─xregexp
│  │                  LICENSE.txt
│  │                  xregexp.js
│  │                  xregexp.min.js
│  │                  
│  ├─assets
│  │  │  demo.css
│  │  │  header.css
│  │  │  skrollr.min.js
│  │  │  
│  │  └─images
│  │      │  bay.jpg
│  │      │  coast.jpg
│  │      │  palmtrees.jpg
│  │      │  sea.jpg
│  │      │  
│  │      └─small
│  │              bay.jpg
│  │              coast.jpg
│  │              palmtrees.jpg
│  │              sea.jpg
│  │              
│  ├─css
│  │      default.css
│  │      htmleaf-demo.css
│  │      normalize.css
│  │      style.css
│  │      
│  ├─css1
│  │      demo.css
│  │      normalize.css
│  │      
│  ├─css2
│  │      default.css
│  │      normalize.css
│  │      
│  ├─img
│  │      1.jpg
│  │      2.jpg
│  │      3.jpg
│  │      4.jpg
│  │      5.jpg
│  │      6.jpg
│  │      bg.jpg
│  │      bg1.jpg
│  │      c2.jpg
│  │      calory.jpg
│  │      circle.jpg
│  │      coast.jpg
│  │      g1+.jpg
│  │      g2+.jpg
│  │      g3+.jpg
│  │      g9+.jpg
│  │      grey2.png
│  │      like.png
│  │      logo.jpg
│  │      rec.jpg
│  │      relation.png
│  │      tree.png
│  │      tt.png
│  │      推荐.jpg
│  │      碳水化合物.jpg
│  │      蛋白质.jpg
│  │      
│  ├─img1
│  │      1.jpg
│  │      2.jpg
│  │      4.jpg
│  │      5.jpg
│  │      7.jpg
│  │      8.jpg
│  │      age.png
│  │      
│  ├─js
│  │      1.jpg
│  │      anime.min.js
│  │      imagesloaded.pkgd.min.js
│  │      main.js
│  │      
│  └─related
│          1.jpg
│          2.jpg
│          
├─templates   //所有前端页面
│      calorie.html
│      carbon.html
│      circle.html
│      decision.html
│      indentify.html
│      load.html
│      main.html
│      old.html
│      protein.html
│      readme.txt
│      recommend.html
│      test.html
│      
├─tree
│  │  1.csv
│  │  main.py
│  │  readme.txt
│  │  Source.gv
│  │  treeone.dot
│  │  
│  └─.idea
│      │  .gitignore
│      │  .name
│      │  decision_tree.iml
│      │  misc.xml
│      │  modules.xml
│      │  workspace.xml
│      │  
│      └─inspectionProfiles
│              profiles_settings.xml
│              Project_Default.xml
│              
└─venv
    │  .gitignore
    │  pyvenv.cfg
    │  
    ├─Lib
    │  └─site-packages
    │      │  decorator.py
    │      │  distutils-precedence.pth
    │      │  pip-21.1.2.virtualenv
    │      │  setuptools-57.0.0.virtualenv
    │      │  wheel-0.36.2.virtualenv
    │      │  _virtualenv.pth
    │      │  _virtualenv.py
    │      │  
    │      ├─cog
    │      │  │  __init__.py
    │      │  │  
    │      │  └─__pycache__
    │      │          __init__.cpython-38.pyc
    │      │          
    │      ├─cog-0.0.3.dist-info
    │      │      INSTALLER
    │      │      METADATA
    │      │      RECORD
    │      │      REQUESTED
    │      │      top_level.txt
    │      │      WHEEL
    │      │      
    │      ├─decorator-4.4.2.dist-info
    │      │      INSTALLER
    │      │      LICENSE.txt
    │      │      METADATA
    │      │      pbr.json
    │      │      RECORD
    │      │      top_level.txt
    │      │      WHEEL
    │      │      
    │      ├─imageio_ffmpeg
    │      │  │  _definitions.py
    │      │  │  _io.py
    │      │  │  _parsing.py
    │      │  │  _utils.py
    │      │  │  __init__.py
    │      │  │  
    │      │  ├─binaries
    │      │  │      ffmpeg-win64-v4.2.2.exe
    │      │  │      README.md
    │      │  │      
    │      │  └─__pycache__
    │      │          _definitions.cpython-38.pyc
    │      │          _io.cpython-38.pyc
    │      │          _parsing.cpython-38.pyc
    │      │          _utils.cpython-38.pyc
    │      │          __init__.cpython-38.pyc
    │      │          
    │      ├─imageio_ffmpeg-0.4.5.dist-info
    │      │      INSTALLER
    │      │      LICENSE
    │      │      METADATA
    │      │      RECORD
    │      │      top_level.txt
    │      │      WHEEL
    │      │      
    │      ├─moviepy
    │      │  │  Clip.py
    │      │  │  compat.py
    │      │  │  config.py
    │      │  │  config_defaults.py
    │      │  │  decorators.py
    │      │  │  editor.py
    │      │  │  tools.py
    │      │  │  utils.py
    │      │  │  version.py
    │      │  │  __init__.py
    │      │  │  
    │      │  ├─audio
    │      │  │  │  AudioClip.py
    │      │  │  │  __init__.py
    │      │  │  │  
    │      │  │  ├─fx
    │      │  │  │  │  audio_fadein.py
    │      │  │  │  │  audio_fadeout.py
    │      │  │  │  │  audio_left_right.py
    │      │  │  │  │  audio_loop.py
    │      │  │  │  │  audio_normalize.py
    │      │  │  │  │  volumex.py
    │      │  │  │  │  __init__.py
    │      │  │  │  │  
    │      │  │  │  ├─all
    │      │  │  │  │  │  __init__.py
    │      │  │  │  │  │  
    │      │  │  │  │  └─__pycache__
    │      │  │  │  │          __init__.cpython-38.pyc
    │      │  │  │  │          
    │      │  │  │  └─__pycache__
    │      │  │  │          audio_fadein.cpython-38.pyc
    │      │  │  │          audio_fadeout.cpython-38.pyc
    │      │  │  │          audio_left_right.cpython-38.pyc
    │      │  │  │          audio_loop.cpython-38.pyc
    │      │  │  │          audio_normalize.cpython-38.pyc
    │      │  │  │          volumex.cpython-38.pyc
    │      │  │  │          __init__.cpython-38.pyc
    │      │  │  │          
    │      │  │  ├─io
    │      │  │  │  │  AudioFileClip.py
    │      │  │  │  │  ffmpeg_audiowriter.py
    │      │  │  │  │  preview.py
    │      │  │  │  │  readers.py
    │      │  │  │  │  __init__.py
    │      │  │  │  │  
    │      │  │  │  └─__pycache__
    │      │  │  │          AudioFileClip.cpython-38.pyc
    │      │  │  │          ffmpeg_audiowriter.cpython-38.pyc
    │      │  │  │          preview.cpython-38.pyc
    │      │  │  │          readers.cpython-38.pyc
    │      │  │  │          __init__.cpython-38.pyc
    │      │  │  │          
    │      │  │  ├─tools
    │      │  │  │  │  cuts.py
    │      │  │  │  │  __init__.py
    │      │  │  │  │  
    │      │  │  │  └─__pycache__
    │      │  │  │          cuts.cpython-38.pyc
    │      │  │  │          __init__.cpython-38.pyc
    │      │  │  │          
    │      │  │  └─__pycache__
    │      │  │          AudioClip.cpython-38.pyc
    │      │  │          __init__.cpython-38.pyc
    │      │  │          
    │      │  ├─video
    │      │  │  │  VideoClip.py
    │      │  │  │  __init__.py
    │      │  │  │  
    │      │  │  ├─compositing
    │      │  │  │  │  CompositeVideoClip.py
    │      │  │  │  │  concatenate.py
    │      │  │  │  │  on_color.py
    │      │  │  │  │  positioning.py
    │      │  │  │  │  transitions.py
    │      │  │  │  │  __init__.py
    │      │  │  │  │  
    │      │  │  │  └─__pycache__
    │      │  │  │          CompositeVideoClip.cpython-38.pyc
    │      │  │  │          concatenate.cpython-38.pyc
    │      │  │  │          on_color.cpython-38.pyc
    │      │  │  │          positioning.cpython-38.pyc
    │      │  │  │          transitions.cpython-38.pyc
    │      │  │  │          __init__.cpython-38.pyc
    │      │  │  │          
    │      │  │  ├─fx
    │      │  │  │  │  accel_decel.py
    │      │  │  │  │  blackwhite.py
    │      │  │  │  │  blink.py
    │      │  │  │  │  colorx.py
    │      │  │  │  │  crop.py
    │      │  │  │  │  even_size.py
    │      │  │  │  │  fadein.py
    │      │  │  │  │  fadeout.py
    │      │  │  │  │  freeze.py
    │      │  │  │  │  freeze_region.py
    │      │  │  │  │  gamma_corr.py
    │      │  │  │  │  headblur.py
    │      │  │  │  │  invert_colors.py
    │      │  │  │  │  loop.py
    │      │  │  │  │  lum_contrast.py
    │      │  │  │  │  make_loopable.py
    │      │  │  │  │  margin.py
    │      │  │  │  │  mask_and.py
    │      │  │  │  │  mask_color.py
    │      │  │  │  │  mask_or.py
    │      │  │  │  │  mirror_x.py
    │      │  │  │  │  mirror_y.py
    │      │  │  │  │  painting.py
    │      │  │  │  │  resize.py
    │      │  │  │  │  rotate.py
    │      │  │  │  │  scroll.py
    │      │  │  │  │  speedx.py
    │      │  │  │  │  supersample.py
    │      │  │  │  │  time_mirror.py
    │      │  │  │  │  time_symmetrize.py
    │      │  │  │  │  __init__.py
    │      │  │  │  │  
    │      │  │  │  ├─all
    │      │  │  │  │  │  __init__.py
    │      │  │  │  │  │  
    │      │  │  │  │  └─__pycache__
    │      │  │  │  │          __init__.cpython-38.pyc
    │      │  │  │  │          
    │      │  │  │  └─__pycache__
    │      │  │  │          accel_decel.cpython-38.pyc
    │      │  │  │          blackwhite.cpython-38.pyc
    │      │  │  │          blink.cpython-38.pyc
    │      │  │  │          colorx.cpython-38.pyc
    │      │  │  │          crop.cpython-38.pyc
    │      │  │  │          even_size.cpython-38.pyc
    │      │  │  │          fadein.cpython-38.pyc
    │      │  │  │          fadeout.cpython-38.pyc
    │      │  │  │          freeze.cpython-38.pyc
    │      │  │  │          freeze_region.cpython-38.pyc
    │      │  │  │          gamma_corr.cpython-38.pyc
    │      │  │  │          headblur.cpython-38.pyc
    │      │  │  │          invert_colors.cpython-38.pyc
    │      │  │  │          loop.cpython-38.pyc
    │      │  │  │          lum_contrast.cpython-38.pyc
    │      │  │  │          make_loopable.cpython-38.pyc
    │      │  │  │          margin.cpython-38.pyc
    │      │  │  │          mask_and.cpython-38.pyc
    │      │  │  │          mask_color.cpython-38.pyc
    │      │  │  │          mask_or.cpython-38.pyc
    │      │  │  │          mirror_x.cpython-38.pyc
    │      │  │  │          mirror_y.cpython-38.pyc
    │      │  │  │          painting.cpython-38.pyc
    │      │  │  │          resize.cpython-38.pyc
    │      │  │  │          rotate.cpython-38.pyc
    │      │  │  │          scroll.cpython-38.pyc
    │      │  │  │          speedx.cpython-38.pyc
    │      │  │  │          supersample.cpython-38.pyc
    │      │  │  │          time_mirror.cpython-38.pyc
    │      │  │  │          time_symmetrize.cpython-38.pyc
    │      │  │  │          __init__.cpython-38.pyc
    │      │  │  │          
    │      │  │  ├─io
    │      │  │  │  │  bindings.py
    │      │  │  │  │  downloader.py
    │      │  │  │  │  ffmpeg_reader.py
    │      │  │  │  │  ffmpeg_tools.py
    │      │  │  │  │  ffmpeg_writer.py
    │      │  │  │  │  gif_writers.py
    │      │  │  │  │  html_tools.py
    │      │  │  │  │  ImageSequenceClip.py
    │      │  │  │  │  preview.py
    │      │  │  │  │  sliders.py
    │      │  │  │  │  VideoFileClip.py
    │      │  │  │  │  __init__.py
    │      │  │  │  │  
    │      │  │  │  └─__pycache__
    │      │  │  │          bindings.cpython-38.pyc
    │      │  │  │          downloader.cpython-38.pyc
    │      │  │  │          ffmpeg_reader.cpython-38.pyc
    │      │  │  │          ffmpeg_tools.cpython-38.pyc
    │      │  │  │          ffmpeg_writer.cpython-38.pyc
    │      │  │  │          gif_writers.cpython-38.pyc
    │      │  │  │          html_tools.cpython-38.pyc
    │      │  │  │          ImageSequenceClip.cpython-38.pyc
    │      │  │  │          preview.cpython-38.pyc
    │      │  │  │          sliders.cpython-38.pyc
    │      │  │  │          VideoFileClip.cpython-38.pyc
    │      │  │  │          __init__.cpython-38.pyc
    │      │  │  │          
    │      │  │  ├─tools
    │      │  │  │  │  credits.py
    │      │  │  │  │  cuts.py
    │      │  │  │  │  drawing.py
    │      │  │  │  │  interpolators.py
    │      │  │  │  │  segmenting.py
    │      │  │  │  │  subtitles.py
    │      │  │  │  │  tracking.py
    │      │  │  │  │  __init__.py
    │      │  │  │  │  
    │      │  │  │  └─__pycache__
    │      │  │  │          credits.cpython-38.pyc
    │      │  │  │          cuts.cpython-38.pyc
    │      │  │  │          drawing.cpython-38.pyc
    │      │  │  │          interpolators.cpython-38.pyc
    │      │  │  │          segmenting.cpython-38.pyc
    │      │  │  │          subtitles.cpython-38.pyc
    │      │  │  │          tracking.cpython-38.pyc
    │      │  │  │          __init__.cpython-38.pyc
    │      │  │  │          
    │      │  │  └─__pycache__
    │      │  │          VideoClip.cpython-38.pyc
    │      │  │          __init__.cpython-38.pyc
    │      │  │          
    │      │  └─__pycache__
    │      │          Clip.cpython-38.pyc
    │      │          compat.cpython-38.pyc
    │      │          config.cpython-38.pyc
    │      │          config_defaults.cpython-38.pyc
    │      │          decorators.cpython-38.pyc
    │      │          editor.cpython-38.pyc
    │      │          tools.cpython-38.pyc
    │      │          utils.cpython-38.pyc
    │      │          version.cpython-38.pyc
    │      │          __init__.cpython-38.pyc
    │      │          
    │      ├─moviepy-1.0.3.dist-info
    │      │      INSTALLER
    │      │      LICENCE.txt
    │      │      METADATA
    │      │      RECORD
    │      │      REQUESTED
    │      │      top_level.txt
    │      │      WHEEL
    │      │      
    │      ├─pip
    │      │  │  py.typed
    │      │  │  __init__.py
    │      │  │  __main__.py
    │      │  │  
    │      │  ├─_internal
    │      │  │  │  build_env.py
    │      │  │  │  cache.py
    │      │  │  │  configuration.py
    │      │  │  │  exceptions.py
    │      │  │  │  main.py
    │      │  │  │  pyproject.py
    │      │  │  │  self_outdated_check.py
    │      │  │  │  wheel_builder.py
    │      │  │  │  __init__.py
    │      │  │  │  
    │      │  │  ├─cli
    │      │  │  │      autocompletion.py
    │      │  │  │      base_command.py
    │      │  │  │      cmdoptions.py
    │      │  │  │      command_context.py
    │      │  │  │      main.py
    │      │  │  │      main_parser.py
    │      │  │  │      parser.py
    │      │  │  │      progress_bars.py
    │      │  │  │      req_command.py
    │      │  │  │      spinners.py
    │      │  │  │      status_codes.py
    │      │  │  │      __init__.py
    │      │  │  │      
    │      │  │  ├─commands
    │      │  │  │      cache.py
    │      │  │  │      check.py
    │      │  │  │      completion.py
    │      │  │  │      configuration.py
    │      │  │  │      debug.py
    │      │  │  │      download.py
    │      │  │  │      freeze.py
    │      │  │  │      hash.py
    │      │  │  │      help.py
    │      │  │  │      install.py
    │      │  │  │      list.py
    │      │  │  │      search.py
    │      │  │  │      show.py
    │      │  │  │      uninstall.py
    │      │  │  │      wheel.py
    │      │  │  │      __init__.py
    │      │  │  │      
    │      │  │  ├─distributions
    │      │  │  │      base.py
    │      │  │  │      installed.py
    │      │  │  │      sdist.py
    │      │  │  │      wheel.py
    │      │  │  │      __init__.py
    │      │  │  │      
    │      │  │  ├─index
    │      │  │  │      collector.py
    │      │  │  │      package_finder.py
    │      │  │  │      sources.py
    │      │  │  │      __init__.py
    │      │  │  │      
    │      │  │  ├─locations
    │      │  │  │      base.py
    │      │  │  │      _distutils.py
    │      │  │  │      _sysconfig.py
    │      │  │  │      __init__.py
    │      │  │  │      
    │      │  │  ├─metadata
    │      │  │  │      base.py
    │      │  │  │      pkg_resources.py
    │      │  │  │      __init__.py
    │      │  │  │      
    │      │  │  ├─models
    │      │  │  │      candidate.py
    │      │  │  │      direct_url.py
    │      │  │  │      format_control.py
    │      │  │  │      index.py
    │      │  │  │      link.py
    │      │  │  │      scheme.py
    │      │  │  │      search_scope.py
    │      │  │  │      selection_prefs.py
    │      │  │  │      target_python.py
    │      │  │  │      wheel.py
    │      │  │  │      __init__.py
    │      │  │  │      
    │      │  │  ├─network
    │      │  │  │      auth.py
    │      │  │  │      cache.py
    │      │  │  │      download.py
    │      │  │  │      lazy_wheel.py
    │      │  │  │      session.py
    │      │  │  │      utils.py
    │      │  │  │      xmlrpc.py
    │      │  │  │      __init__.py
    │      │  │  │      
    │      │  │  ├─operations
    │      │  │  │  │  check.py
    │      │  │  │  │  freeze.py
    │      │  │  │  │  prepare.py
    │      │  │  │  │  __init__.py
    │      │  │  │  │  
    │      │  │  │  ├─build
    │      │  │  │  │      metadata.py
    │      │  │  │  │      metadata_legacy.py
    │      │  │  │  │      wheel.py
    │      │  │  │  │      wheel_legacy.py
    │      │  │  │  │      __init__.py
    │      │  │  │  │      
    │      │  │  │  └─install
    │      │  │  │          editable_legacy.py
    │      │  │  │          legacy.py
    │      │  │  │          wheel.py
    │      │  │  │          __init__.py
    │      │  │  │          
    │      │  │  ├─req
    │      │  │  │      constructors.py
    │      │  │  │      req_file.py
    │      │  │  │      req_install.py
    │      │  │  │      req_set.py
    │      │  │  │      req_tracker.py
    │      │  │  │      req_uninstall.py
    │      │  │  │      __init__.py
    │      │  │  │      
    │      │  │  ├─resolution
    │      │  │  │  │  base.py
    │      │  │  │  │  __init__.py
    │      │  │  │  │  
    │      │  │  │  ├─legacy
    │      │  │  │  │      resolver.py
    │      │  │  │  │      __init__.py
    │      │  │  │  │      
    │      │  │  │  └─resolvelib
    │      │  │  │          base.py
    │      │  │  │          candidates.py
    │      │  │  │          factory.py
    │      │  │  │          found_candidates.py
    │      │  │  │          provider.py
    │      │  │  │          reporter.py
    │      │  │  │          requirements.py
    │      │  │  │          resolver.py
    │      │  │  │          __init__.py
    │      │  │  │          
    │      │  │  ├─utils
    │      │  │  │      appdirs.py
    │      │  │  │      compat.py
    │      │  │  │      compatibility_tags.py
    │      │  │  │      datetime.py
    │      │  │  │      deprecation.py
    │      │  │  │      direct_url_helpers.py
    │      │  │  │      distutils_args.py
    │      │  │  │      encoding.py
    │      │  │  │      entrypoints.py
    │      │  │  │      filesystem.py
    │      │  │  │      filetypes.py
    │      │  │  │      glibc.py
    │      │  │  │      hashes.py
    │      │  │  │      inject_securetransport.py
    │      │  │  │      logging.py
    │      │  │  │      misc.py
    │      │  │  │      models.py
    │      │  │  │      packaging.py
    │      │  │  │      parallel.py
    │      │  │  │      pkg_resources.py
    │      │  │  │      setuptools_build.py
    │      │  │  │      subprocess.py
    │      │  │  │      temp_dir.py
    │      │  │  │      unpacking.py
    │      │  │  │      urls.py
    │      │  │  │      virtualenv.py
    │      │  │  │      wheel.py
    │      │  │  │      __init__.py
    │      │  │  │      
    │      │  │  └─vcs
    │      │  │          bazaar.py
    │      │  │          git.py
    │      │  │          mercurial.py
    │      │  │          subversion.py
    │      │  │          versioncontrol.py
    │      │  │          __init__.py
    │      │  │          
    │      │  └─_vendor
    │      │      │  appdirs.py
    │      │      │  distro.py
    │      │      │  pyparsing.py
    │      │      │  six.py
    │      │      │  vendor.txt
    │      │      │  __init__.py
    │      │      │  
    │      │      ├─cachecontrol
    │      │      │  │  adapter.py
    │      │      │  │  cache.py
    │      │      │  │  compat.py
    │      │      │  │  controller.py
    │      │      │  │  filewrapper.py
    │      │      │  │  heuristics.py
    │      │      │  │  serialize.py
    │      │      │  │  wrapper.py
    │      │      │  │  _cmd.py
    │      │      │  │  __init__.py
    │      │      │  │  
    │      │      │  └─caches
    │      │      │          file_cache.py
    │      │      │          redis_cache.py
    │      │      │          __init__.py
    │      │      │          
    │      │      ├─certifi
    │      │      │      cacert.pem
    │      │      │      core.py
    │      │      │      __init__.py
    │      │      │      __main__.py
    │      │      │      
    │      │      ├─chardet
    │      │      │  │  big5freq.py
    │      │      │  │  big5prober.py
    │      │      │  │  chardistribution.py
    │      │      │  │  charsetgroupprober.py
    │      │      │  │  charsetprober.py
    │      │      │  │  codingstatemachine.py
    │      │      │  │  compat.py
    │      │      │  │  cp949prober.py
    │      │      │  │  enums.py
    │      │      │  │  escprober.py
    │      │      │  │  escsm.py
    │      │      │  │  eucjpprober.py
    │      │      │  │  euckrfreq.py
    │      │      │  │  euckrprober.py
    │      │      │  │  euctwfreq.py
    │      │      │  │  euctwprober.py
    │      │      │  │  gb2312freq.py
    │      │      │  │  gb2312prober.py
    │      │      │  │  hebrewprober.py
    │      │      │  │  jisfreq.py
    │      │      │  │  jpcntx.py
    │      │      │  │  langbulgarianmodel.py
    │      │      │  │  langgreekmodel.py
    │      │      │  │  langhebrewmodel.py
    │      │      │  │  langhungarianmodel.py
    │      │      │  │  langrussianmodel.py
    │      │      │  │  langthaimodel.py
    │      │      │  │  langturkishmodel.py
    │      │      │  │  latin1prober.py
    │      │      │  │  mbcharsetprober.py
    │      │      │  │  mbcsgroupprober.py
    │      │      │  │  mbcssm.py
    │      │      │  │  sbcharsetprober.py
    │      │      │  │  sbcsgroupprober.py
    │      │      │  │  sjisprober.py
    │      │      │  │  universaldetector.py
    │      │      │  │  utf8prober.py
    │      │      │  │  version.py
    │      │      │  │  __init__.py
    │      │      │  │  
    │      │      │  ├─cli
    │      │      │  │      chardetect.py
    │      │      │  │      __init__.py
    │      │      │  │      
    │      │      │  └─metadata
    │      │      │          languages.py
    │      │      │          __init__.py
    │      │      │          
    │      │      ├─colorama
    │      │      │      ansi.py
    │      │      │      ansitowin32.py
    │      │      │      initialise.py
    │      │      │      win32.py
    │      │      │      winterm.py
    │      │      │      __init__.py
    │      │      │      
    │      │      ├─distlib
    │      │      │  │  compat.py
    │      │      │  │  database.py
    │      │      │  │  index.py
    │      │      │  │  locators.py
    │      │      │  │  manifest.py
    │      │      │  │  markers.py
    │      │      │  │  metadata.py
    │      │      │  │  resources.py
    │      │      │  │  scripts.py
    │      │      │  │  t32.exe
    │      │      │  │  t64.exe
    │      │      │  │  util.py
    │      │      │  │  version.py
    │      │      │  │  w32.exe
    │      │      │  │  w64.exe
    │      │      │  │  wheel.py
    │      │      │  │  __init__.py
    │      │      │  │  
    │      │      │  └─_backport
    │      │      │          misc.py
    │      │      │          shutil.py
    │      │      │          sysconfig.cfg
    │      │      │          sysconfig.py
    │      │      │          tarfile.py
    │      │      │          __init__.py
    │      │      │          
    │      │      ├─html5lib
    │      │      │  │  constants.py
    │      │      │  │  html5parser.py
    │      │      │  │  serializer.py
    │      │      │  │  _ihatexml.py
    │      │      │  │  _inputstream.py
    │      │      │  │  _tokenizer.py
    │      │      │  │  _utils.py
    │      │      │  │  __init__.py
    │      │      │  │  
    │      │      │  ├─filters
    │      │      │  │      alphabeticalattributes.py
    │      │      │  │      base.py
    │      │      │  │      inject_meta_charset.py
    │      │      │  │      lint.py
    │      │      │  │      optionaltags.py
    │      │      │  │      sanitizer.py
    │      │      │  │      whitespace.py
    │      │      │  │      __init__.py
    │      │      │  │      
    │      │      │  ├─treeadapters
    │      │      │  │      genshi.py
    │      │      │  │      sax.py
    │      │      │  │      __init__.py
    │      │      │  │      
    │      │      │  ├─treebuilders
    │      │      │  │      base.py
    │      │      │  │      dom.py
    │      │      │  │      etree.py
    │      │      │  │      etree_lxml.py
    │      │      │  │      __init__.py
    │      │      │  │      
    │      │      │  ├─treewalkers
    │      │      │  │      base.py
    │      │      │  │      dom.py
    │      │      │  │      etree.py
    │      │      │  │      etree_lxml.py
    │      │      │  │      genshi.py
    │      │      │  │      __init__.py
    │      │      │  │      
    │      │      │  └─_trie
    │      │      │          py.py
    │      │      │          _base.py
    │      │      │          __init__.py
    │      │      │          
    │      │      ├─idna
    │      │      │      codec.py
    │      │      │      compat.py
    │      │      │      core.py
    │      │      │      idnadata.py
    │      │      │      intranges.py
    │      │      │      package_data.py
    │      │      │      uts46data.py
    │      │      │      __init__.py
    │      │      │      
    │      │      ├─msgpack
    │      │      │      exceptions.py
    │      │      │      ext.py
    │      │      │      fallback.py
    │      │      │      _version.py
    │      │      │      __init__.py
    │      │      │      
    │      │      ├─packaging
    │      │      │      markers.py
    │      │      │      requirements.py
    │      │      │      specifiers.py
    │      │      │      tags.py
    │      │      │      utils.py
    │      │      │      version.py
    │      │      │      _compat.py
    │      │      │      _structures.py
    │      │      │      _typing.py
    │      │      │      __about__.py
    │      │      │      __init__.py
    │      │      │      
    │      │      ├─pep517
    │      │      │  │  build.py
    │      │      │  │  check.py
    │      │      │  │  colorlog.py
    │      │      │  │  compat.py
    │      │      │  │  dirtools.py
    │      │      │  │  envbuild.py
    │      │      │  │  meta.py
    │      │      │  │  wrappers.py
    │      │      │  │  __init__.py
    │      │      │  │  
    │      │      │  └─in_process
    │      │      │          _in_process.py
    │      │      │          __init__.py
    │      │      │          
    │      │      ├─pkg_resources
    │      │      │      py31compat.py
    │      │      │      __init__.py
    │      │      │      
    │      │      ├─progress
    │      │      │      bar.py
    │      │      │      counter.py
    │      │      │      spinner.py
    │      │      │      __init__.py
    │      │      │      
    │      │      ├─requests
    │      │      │      adapters.py
    │      │      │      api.py
    │      │      │      auth.py
    │      │      │      certs.py
    │      │      │      compat.py
    │      │      │      cookies.py
    │      │      │      exceptions.py
    │      │      │      help.py
    │      │      │      hooks.py
    │      │      │      models.py
    │      │      │      packages.py
    │      │      │      sessions.py
    │      │      │      status_codes.py
    │      │      │      structures.py
    │      │      │      utils.py
    │      │      │      _internal_utils.py
    │      │      │      __init__.py
    │      │      │      __version__.py
    │      │      │      
    │      │      ├─resolvelib
    │      │      │  │  providers.py
    │      │      │  │  reporters.py
    │      │      │  │  resolvers.py
    │      │      │  │  structs.py
    │      │      │  │  __init__.py
    │      │      │  │  
    │      │      │  └─compat
    │      │      │          collections_abc.py
    │      │      │          __init__.py
    │      │      │          
    │      │      ├─tenacity
    │      │      │      after.py
    │      │      │      before.py
    │      │      │      before_sleep.py
    │      │      │      compat.py
    │      │      │      nap.py
    │      │      │      retry.py
    │      │      │      stop.py
    │      │      │      tornadoweb.py
    │      │      │      wait.py
    │      │      │      _asyncio.py
    │      │      │      _utils.py
    │      │      │      __init__.py
    │      │      │      
    │      │      ├─toml
    │      │      │      decoder.py
    │      │      │      encoder.py
    │      │      │      ordered.py
    │      │      │      tz.py
    │      │      │      __init__.py
    │      │      │      
    │      │      ├─urllib3
    │      │      │  │  connection.py
    │      │      │  │  connectionpool.py
    │      │      │  │  exceptions.py
    │      │      │  │  fields.py
    │      │      │  │  filepost.py
    │      │      │  │  poolmanager.py
    │      │      │  │  request.py
    │      │      │  │  response.py
    │      │      │  │  _collections.py
    │      │      │  │  _version.py
    │      │      │  │  __init__.py
    │      │      │  │  
    │      │      │  ├─contrib
    │      │      │  │  │  appengine.py
    │      │      │  │  │  ntlmpool.py
    │      │      │  │  │  pyopenssl.py
    │      │      │  │  │  securetransport.py
    │      │      │  │  │  socks.py
    │      │      │  │  │  _appengine_environ.py
    │      │      │  │  │  __init__.py
    │      │      │  │  │  
    │      │      │  │  └─_securetransport
    │      │      │  │          bindings.py
    │      │      │  │          low_level.py
    │      │      │  │          __init__.py
    │      │      │  │          
    │      │      │  ├─packages
    │      │      │  │  │  six.py
    │      │      │  │  │  __init__.py
    │      │      │  │  │  
    │      │      │  │  ├─backports
    │      │      │  │  │      makefile.py
    │      │      │  │  │      __init__.py
    │      │      │  │  │      
    │      │      │  │  └─ssl_match_hostname
    │      │      │  │          _implementation.py
    │      │      │  │          __init__.py
    │      │      │  │          
    │      │      │  └─util
    │      │      │          connection.py
    │      │      │          proxy.py
    │      │      │          queue.py
    │      │      │          request.py
    │      │      │          response.py
    │      │      │          retry.py
    │      │      │          ssltransport.py
    │      │      │          ssl_.py
    │      │      │          timeout.py
    │      │      │          url.py
    │      │      │          wait.py
    │      │      │          __init__.py
    │      │      │          
    │      │      └─webencodings
    │      │              labels.py
    │      │              mklabels.py
    │      │              tests.py
    │      │              x_user_defined.py
    │      │              __init__.py
    │      │              
    │      ├─pip-21.1.2.dist-info
    │      │      entry_points.txt
    │      │      INSTALLER
    │      │      LICENSE.txt
    │      │      METADATA
    │      │      RECORD
    │      │      top_level.txt
    │      │      WHEEL
    │      │      
    │      ├─pkg_resources
    │      │  │  __init__.py
    │      │  │  
    │      │  ├─extern
    │      │  │  │  __init__.py
    │      │  │  │  
    │      │  │  └─__pycache__
    │      │  │          __init__.cpython-38.pyc
    │      │  │          
    │      │  ├─tests
    │      │  │  └─data
    │      │  │      └─my-test-package-source
    │      │  │              setup.py
    │      │  │              
    │      │  ├─_vendor
    │      │  │  │  appdirs.py
    │      │  │  │  pyparsing.py
    │      │  │  │  __init__.py
    │      │  │  │  
    │      │  │  ├─packaging
    │      │  │  │  │  markers.py
    │      │  │  │  │  requirements.py
    │      │  │  │  │  specifiers.py
    │      │  │  │  │  tags.py
    │      │  │  │  │  utils.py
    │      │  │  │  │  version.py
    │      │  │  │  │  _compat.py
    │      │  │  │  │  _structures.py
    │      │  │  │  │  _typing.py
    │      │  │  │  │  __about__.py
    │      │  │  │  │  __init__.py
    │      │  │  │  │  
    │      │  │  │  └─__pycache__
    │      │  │  │          markers.cpython-38.pyc
    │      │  │  │          requirements.cpython-38.pyc
    │      │  │  │          specifiers.cpython-38.pyc
    │      │  │  │          utils.cpython-38.pyc
    │      │  │  │          version.cpython-38.pyc
    │      │  │  │          _compat.cpython-38.pyc
    │      │  │  │          _structures.cpython-38.pyc
    │      │  │  │          _typing.cpython-38.pyc
    │      │  │  │          __about__.cpython-38.pyc
    │      │  │  │          __init__.cpython-38.pyc
    │      │  │  │          
    │      │  │  └─__pycache__
    │      │  │          appdirs.cpython-38.pyc
    │      │  │          pyparsing.cpython-38.pyc
    │      │  │          __init__.cpython-38.pyc
    │      │  │          
    │      │  └─__pycache__
    │      │          __init__.cpython-38.pyc
    │      │          
    │      ├─proglog
    │      │  │  proglog.py
    │      │  │  version.py
    │      │  │  __init__.py
    │      │  │  
    │      │  └─__pycache__
    │      │          proglog.cpython-38.pyc
    │      │          version.cpython-38.pyc
    │      │          __init__.cpython-38.pyc
    │      │          
    │      ├─proglog-0.1.9.dist-info
    │      │      INSTALLER
    │      │      LICENCE.txt
    │      │      METADATA
    │      │      RECORD
    │      │      top_level.txt
    │      │      WHEEL
    │      │      
    │      ├─setuptools
    │      │  │  archive_util.py
    │      │  │  build_meta.py
    │      │  │  cli-32.exe
    │      │  │  cli-64.exe
    │      │  │  cli.exe
    │      │  │  config.py
    │      │  │  depends.py
    │      │  │  dep_util.py
    │      │  │  dist.py
    │      │  │  errors.py
    │      │  │  extension.py
    │      │  │  glob.py
    │      │  │  gui-32.exe
    │      │  │  gui-64.exe
    │      │  │  gui.exe
    │      │  │  installer.py
    │      │  │  launch.py
    │      │  │  lib2to3_ex.py
    │      │  │  monkey.py
    │      │  │  msvc.py
    │      │  │  namespaces.py
    │      │  │  package_index.py
    │      │  │  py34compat.py
    │      │  │  sandbox.py
    │      │  │  script (dev).tmpl
    │      │  │  script.tmpl
    │      │  │  ssl_support.py
    │      │  │  unicode_utils.py
    │      │  │  version.py
    │      │  │  wheel.py
    │      │  │  windows_support.py
    │      │  │  _deprecation_warning.py
    │      │  │  _imp.py
    │      │  │  __init__.py
    │      │  │  
    │      │  ├─command
    │      │  │  │  alias.py
    │      │  │  │  bdist_egg.py
    │      │  │  │  bdist_rpm.py
    │      │  │  │  build_clib.py
    │      │  │  │  build_ext.py
    │      │  │  │  build_py.py
    │      │  │  │  develop.py
    │      │  │  │  dist_info.py
    │      │  │  │  easy_install.py
    │      │  │  │  egg_info.py
    │      │  │  │  install.py
    │      │  │  │  install_egg_info.py
    │      │  │  │  install_lib.py
    │      │  │  │  install_scripts.py
    │      │  │  │  launcher manifest.xml
    │      │  │  │  py36compat.py
    │      │  │  │  register.py
    │      │  │  │  rotate.py
    │      │  │  │  saveopts.py
    │      │  │  │  sdist.py
    │      │  │  │  setopt.py
    │      │  │  │  test.py
    │      │  │  │  upload.py
    │      │  │  │  upload_docs.py
    │      │  │  │  __init__.py
    │      │  │  │  
    │      │  │  └─__pycache__
    │      │  │          __init__.cpython-38.pyc
    │      │  │          
    │      │  ├─extern
    │      │  │  │  __init__.py
    │      │  │  │  
    │      │  │  └─__pycache__
    │      │  │          __init__.cpython-38.pyc
    │      │  │          
    │      │  ├─_distutils
    │      │  │  │  archive_util.py
    │      │  │  │  bcppcompiler.py
    │      │  │  │  ccompiler.py
    │      │  │  │  cmd.py
    │      │  │  │  config.py
    │      │  │  │  core.py
    │      │  │  │  cygwinccompiler.py
    │      │  │  │  debug.py
    │      │  │  │  dep_util.py
    │      │  │  │  dir_util.py
    │      │  │  │  dist.py
    │      │  │  │  errors.py
    │      │  │  │  extension.py
    │      │  │  │  fancy_getopt.py
    │      │  │  │  filelist.py
    │      │  │  │  file_util.py
    │      │  │  │  log.py
    │      │  │  │  msvc9compiler.py
    │      │  │  │  msvccompiler.py
    │      │  │  │  py35compat.py
    │      │  │  │  py38compat.py
    │      │  │  │  spawn.py
    │      │  │  │  sysconfig.py
    │      │  │  │  text_file.py
    │      │  │  │  unixccompiler.py
    │      │  │  │  util.py
    │      │  │  │  version.py
    │      │  │  │  versionpredicate.py
    │      │  │  │  _msvccompiler.py
    │      │  │  │  __init__.py
    │      │  │  │  
    │      │  │  ├─command
    │      │  │  │  │  bdist.py
    │      │  │  │  │  bdist_dumb.py
    │      │  │  │  │  bdist_msi.py
    │      │  │  │  │  bdist_rpm.py
    │      │  │  │  │  bdist_wininst.py
    │      │  │  │  │  build.py
    │      │  │  │  │  build_clib.py
    │      │  │  │  │  build_ext.py
    │      │  │  │  │  build_py.py
    │      │  │  │  │  build_scripts.py
    │      │  │  │  │  check.py
    │      │  │  │  │  clean.py
    │      │  │  │  │  config.py
    │      │  │  │  │  install.py
    │      │  │  │  │  install_data.py
    │      │  │  │  │  install_egg_info.py
    │      │  │  │  │  install_headers.py
    │      │  │  │  │  install_lib.py
    │      │  │  │  │  install_scripts.py
    │      │  │  │  │  py37compat.py
    │      │  │  │  │  register.py
    │      │  │  │  │  sdist.py
    │      │  │  │  │  upload.py
    │      │  │  │  │  __init__.py
    │      │  │  │  │  
    │      │  │  │  └─__pycache__
    │      │  │  │          bdist.cpython-38.pyc
    │      │  │  │          __init__.cpython-38.pyc
    │      │  │  │          
    │      │  │  └─__pycache__
    │      │  │          archive_util.cpython-38.pyc
    │      │  │          ccompiler.cpython-38.pyc
    │      │  │          cmd.cpython-38.pyc
    │      │  │          config.cpython-38.pyc
    │      │  │          core.cpython-38.pyc
    │      │  │          debug.cpython-38.pyc
    │      │  │          dep_util.cpython-38.pyc
    │      │  │          dir_util.cpython-38.pyc
    │      │  │          dist.cpython-38.pyc
    │      │  │          errors.cpython-38.pyc
    │      │  │          extension.cpython-38.pyc
    │      │  │          fancy_getopt.cpython-38.pyc
    │      │  │          filelist.cpython-38.pyc
    │      │  │          file_util.cpython-38.pyc
    │      │  │          log.cpython-38.pyc
    │      │  │          msvc9compiler.cpython-38.pyc
    │      │  │          py35compat.cpython-38.pyc
    │      │  │          spawn.cpython-38.pyc
    │      │  │          util.cpython-38.pyc
    │      │  │          version.cpython-38.pyc
    │      │  │          _msvccompiler.cpython-38.pyc
    │      │  │          __init__.cpython-38.pyc
    │      │  │          
    │      │  ├─_vendor
    │      │  │  │  ordered_set.py
    │      │  │  │  pyparsing.py
    │      │  │  │  __init__.py
    │      │  │  │  
    │      │  │  ├─more_itertools
    │      │  │  │  │  more.py
    │      │  │  │  │  recipes.py
    │      │  │  │  │  __init__.py
    │      │  │  │  │  
    │      │  │  │  └─__pycache__
    │      │  │  │          more.cpython-38.pyc
    │      │  │  │          recipes.cpython-38.pyc
    │      │  │  │          __init__.cpython-38.pyc
    │      │  │  │          
    │      │  │  ├─packaging
    │      │  │  │  │  markers.py
    │      │  │  │  │  requirements.py
    │      │  │  │  │  specifiers.py
    │      │  │  │  │  tags.py
    │      │  │  │  │  utils.py
    │      │  │  │  │  version.py
    │      │  │  │  │  _compat.py
    │      │  │  │  │  _structures.py
    │      │  │  │  │  _typing.py
    │      │  │  │  │  __about__.py
    │      │  │  │  │  __init__.py
    │      │  │  │  │  
    │      │  │  │  └─__pycache__
    │      │  │  │          specifiers.cpython-38.pyc
    │      │  │  │          utils.cpython-38.pyc
    │      │  │  │          version.cpython-38.pyc
    │      │  │  │          _compat.cpython-38.pyc
    │      │  │  │          _structures.cpython-38.pyc
    │      │  │  │          _typing.cpython-38.pyc
    │      │  │  │          __about__.cpython-38.pyc
    │      │  │  │          __init__.cpython-38.pyc
    │      │  │  │          
    │      │  │  └─__pycache__
    │      │  │          ordered_set.cpython-38.pyc
    │      │  │          __init__.cpython-38.pyc
    │      │  │          
    │      │  └─__pycache__
    │      │          config.cpython-38.pyc
    │      │          depends.cpython-38.pyc
    │      │          dist.cpython-38.pyc
    │      │          extension.cpython-38.pyc
    │      │          monkey.cpython-38.pyc
    │      │          msvc.cpython-38.pyc
    │      │          py34compat.cpython-38.pyc
    │      │          version.cpython-38.pyc
    │      │          windows_support.cpython-38.pyc
    │      │          _deprecation_warning.cpython-38.pyc
    │      │          _imp.cpython-38.pyc
    │      │          __init__.cpython-38.pyc
    │      │          
    │      ├─setuptools-57.0.0.dist-info
    │      │      dependency_links.txt
    │      │      entry_points.txt
    │      │      INSTALLER
    │      │      LICENSE
    │      │      METADATA
    │      │      RECORD
    │      │      top_level.txt
    │      │      WHEEL
    │      │      
    │      ├─wheel
    │      │  │  bdist_wheel.py
    │      │  │  macosx_libfile.py
    │      │  │  metadata.py
    │      │  │  pkginfo.py
    │      │  │  util.py
    │      │  │  wheelfile.py
    │      │  │  __init__.py
    │      │  │  __main__.py
    │      │  │  
    │      │  ├─cli
    │      │  │      convert.py
    │      │  │      pack.py
    │      │  │      unpack.py
    │      │  │      __init__.py
    │      │  │      
    │      │  └─vendored
    │      │      │  __init__.py
    │      │      │  
    │      │      └─packaging
    │      │              tags.py
    │      │              _typing.py
    │      │              __init__.py
    │      │              
    │      ├─wheel-0.36.2.dist-info
    │      │      entry_points.txt
    │      │      INSTALLER
    │      │      LICENSE.txt
    │      │      METADATA
    │      │      RECORD
    │      │      top_level.txt
    │      │      WHEEL
    │      │      
    │      ├─_distutils_hack
    │      │  │  override.py
    │      │  │  __init__.py
    │      │  │  
    │      │  └─__pycache__
    │      │          override.cpython-38.pyc
    │      │          __init__.cpython-38.pyc
    │      │          
    │      └─__pycache__
    │              decorator.cpython-38.pyc
    │              _virtualenv.cpython-38.pyc
    │              
    └─Scripts
            activate
            activate.bat
            activate.fish
            activate.ps1
            activate.xsh
            activate_this.py
            deactivate.bat
            pip-3.8.exe
            pip.exe
            pip3.8.exe
            pip3.exe
            pydoc.bat
            python.exe
            pythonw.exe
            wheel-3.8.exe
            wheel.exe
            wheel3.8.exe
            wheel3.exe
            
