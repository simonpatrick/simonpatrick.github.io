
```java
    @RequestMapping(value = "/check/{userCode}", method = RequestMethod.GET)
    @ResponseBody
    public String checkPassword(@PathVariable int userCode, HttpServletRequest request) {
        String result = fail().toString();
        //判决该员工是否有过修改密码记录
        if(!employeePasswordInfoService.isExistsRecord(userCode)) {
            result = ok().toString();
        }
        //密码是否即将过期
        else if(employeePasswordInfoService.isExistsOutOfDate(userCode)) {
            result = ok().toString();
        }
        //是否跨域
        String jsonCallback = request.getParameter("jsonCallback");
        if(StringUtils.isNotBlank(jsonCallback)) {
            return jsonCallback + "(" + result + ")";
        }
        return result;
    }
```

```xml
<select id="checkPwd" resultClass="empPwdInfo">
      SELECT p.*
        FROM T_OMS_EMPLOYEE_PASSWORD_INFO p with(nolock)
        WHERE p.id =
            (SELECT top 1 id
             FROM T_OMS_EMPLOYEE_PASSWORD_INFO with(nolock)
             WHERE userCode =  #userCode#
             order by updateTime desc
             )
          AND GETDATE() - #warningDate#  > p.updateTime
    </select>

    <select id="isExistsRecord" resultClass="empPwdInfo">
        select top 1 id from T_OMS_EMPLOYEE_PASSWORD_INFO WITH(NOLOCK)
        where userCode = #userCode#
    </select>

```

- checkPassword: what this api used for?
- take two db call? 

