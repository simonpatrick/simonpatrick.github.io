# Bootstrap 
- CSS
- Component
- Javascript

## CSS
- initial-scale =1.0, user-scalable =true
- img-responsive class
```css
.img-responsive{
 display:inline-block;
 height:auto;
 max-width:100%
}
```
inline-block 可以自己定义宽度和高度

- 全局显示，排版和链接
- 媒体查询
```css
@media(min-width:@screen-sm-min)
@media(min-width:@screen-md-min)
@media((min-width:@screen-lg-min) and (max-width:@screen-md-max))
```
-  网格约定
* 超小：
    
    ```<768```,小型 ```>=768``,中型```>=992```,大型```>=1200```
* 以折叠开始，断点以上是水平
* class前缀：.col-xs- .col-sm- .col-md- .col-lg-
* 最大列宽：auto，60px，78px，95px
* 间隙宽度：30px，30px，30px，30px
* 偏移列：col-xs 不支持，col-md-offset-* 使用左边距增加*列
    
- header 
    ```class='lead'```

-     
