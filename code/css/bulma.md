# BulmaCSS
---
### General
- |$Color :: white,black,primary,link,info,success,warning,danger,light,dark
- |$shade :: light,dark
- |$d :: mobile,touch,tablet,desktop,widescreen,fullhd
- |Size|>is-size-$n-/-$d :: n=1,2,3,4,5,6,7 || small,medium,large
- |Utility|>is-$ :: pulled-left/right,radiusless,unselectable,relative
- |Background|>has-background-$color-/-$shade ::
- |Spacing|>$S-$px :: 
    - |$=m-margin,p-padding|
    - |S=x-horizontal,y-vertical,t-top,b-bottom,l-left,r-right|
    - $px:0,1,2,3,4,5,6, {| mt-3:margin top 0.75rem |}

### Text
- |has-text-$color-/-$shade : ^-^
- |has-text-$(pos)-/-d : centered,justified,left,right
- |is-$transform : captitalized,lowercase,uppercase,italic
- |has-text-weight-$bold : light,normal,medium,semibold,bold
- |is-family-$font : sans-serif,monospace,primary,secondary,secondary,code

### Flex
_is-justifycontent-$pos_:flex-start,start,end,center
_is-align-content-$pos_

### Column
- |:: colmns(row) => column(column) || C>c
- |Responsive |> columns.is-$d::mobile
- |Gap |> is-$modifier :: gapless,multiline,1...8(gap),vcentered,centered
- |-Size |> c.is-$size-/-$d|> full,1/2/3-5th,half,1-3rd || 1...12
- |-Offset |> c.is-offset-$size :
- |-Narrow |> c.is-narrow-/-$d :
- |--Nested |> C>c>C>c

## Layout

- |Container |> .container :: is-d::widescreen,max-desktop/widescreen,fluid 
    - |-<{ navbar,hero,section,footer}
- |Level |> (nav).level => L-left/right => L-item || is-mobile
- |Media |> (article).media => (figure).media- left/content/right
- |Hero |> hero => h-head/body/foot || is-$color/$size:medium,large,fullheight
- |Section |> << body && >> container
- |Footer |> footer >> container
- |Tile |> tile.ancestor=>t.parent...=>t.child.(box)... || is-$size :: 1...12||is-vertical 

## Form
- |Input |> .field => (label.is-$size)+(.control.is-$size/loading)=>(input.input.is-$size/$color/rounded/static)|(select)|(button) -< .help
- |-Icon |> control.has-icon-left/right |(INPUT)++ (span.icon.is-$size.is-left/right) => (i.class)
- |-Addons |> f.has-addons-/-center/right => c.input+c.button+c...
- |-Responsive |> c.is-expanded
- |-Group |> f.is-grouped-/-center/right/multiline
- |-Horizontal(forPerRow) |> f => f.is-horzontal => .f-label->(label) + .f-body->.field
- |-Attr |> (fieldset disabled/readonly)
- |Select |> f => c => (span.select.is-fullwidth) => (select) => (option)
- |Textarea|>.f => .c => (textarea.textarea.is-$color/$size.has-fixed-size|rows="n"|diable|readonly)
- |Checkbox/radio|>(label.checkbox/radio)=>(input|checked|disabled)

## Element
- |Block |> .block :: [space for each divide]
- |Box |> .box
- |Button 
    - |.f.has-addons.is-$pos -> .c+.c -> .button.is-$color.is-$size.is-fullwidth/-outlined/-inverted/-rounded/-loading/-static 
    - |-> .buttons>.button |-> button>(span).icon.is-$size>i.fa.fa-icon + (span)

## Component
- s
- |Navbar|>nav.navbar=>[.navbar-brand->.navbar-items/.navbar-burger->span]+[]
