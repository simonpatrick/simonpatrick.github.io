## AccountingController#list
- model.addAttribute("accountingList", aiService.getAccountingList(paramsMap)) ;
- model.addAttribute("accountingCount", aiService.getAccountingCount(paramsMap));

aiService 都是使用去查询accountList，我们将计算太多都给了数据库，数据库实际上水平扩展是最辛苦的.

验证点：

－ 一次SQL
－ 两次SQL的比较

## ApiController#querySalaryByModel

```java
m.put("totalCount", apiSalaryService.totalCount(pMap));
m.put("totalMoney", apiSalaryService.totalMoney(pMap));
m.put("payList",apiSalaryService.querySalaries(pMap));
m.put("isHistory",!SalaryHelper.isCurrent(year,month));
```

```xml
<sqlMap namespace="VApiSalary">
     <select id="querySalary" parameterClass="hashMap" resultClass="vApiSalary">
        select userCode, isnull(taxtotal,0) as pay,isnull(persontax,0) as tax from
       <isEqual property="isHistory" compareValue="true">
          T_Employee_SalaryHistory WITH(NOLOCK)
       </isEqual>
       <isEqual property="isHistory" compareValue="false">
             T_Employee_Salary WITH(NOLOCK)
       </isEqual>
        where salarytype ='工资' and company = '$company$'
        <isNotEqual property="userCode" prepend="and" compareValue="0">
          userCode = $userCode$
        </isNotEqual>
        <isNotEqual property="year" prepend="and" compareValue="0">
            year = $year$ and month = $month$
        </isNotEqual>
     </select>

    <select id="totalCount" parameterClass="hashMap" resultClass="double">
        select count(1) from
        <isEqual property="isHistory" compareValue="true">
            T_Employee_SalaryHistory WITH(NOLOCK)
        </isEqual>
        <isEqual property="isHistory" compareValue="false">
            T_Employee_Salary WITH(NOLOCK)
        </isEqual>
        where salarytype ='工资' and company = '$company$'
        <isNotEqual property="userCode" prepend="and" compareValue="0">
            userCode = $userCode$
        </isNotEqual>
        <isNotEqual property="year" prepend="and" compareValue="0">
            year = $year$ and month = $month$
        </isNotEqual>
     </select>

    <select id="totalMoney" parameterClass="hashMap" resultClass="double">
        select isnull(sum(taxtotal),0) from
        <isEqual property="isHistory" compareValue="true">
            T_Employee_SalaryHistory WITH(NOLOCK)
        </isEqual>
        <isEqual property="isHistory" compareValue="false">
            T_Employee_Salary WITH(NOLOCK)
        </isEqual>
        where salarytype ='工资' and company = '$company$'
        <isNotEqual property="userCode" prepend="and" compareValue="0">
            userCode = $userCode$
        </isNotEqual>
        <isNotEqual property="year" prepend="and" compareValue="0">
            year = $year$ and month = $month$
        </isNotEqual>
     </select>
</sqlMap>
```
这样的开销真的好吗？

## Pre-Statement

安装mybatis以下的方式不知道是不是使用prestatement来访问？

```xml
<select id="querySalary" parameterClass="hashMap" resultClass="vApiSalary">
        select userCode, isnull(taxtotal,0) as pay,isnull(persontax,0) as tax from
       <isEqual property="isHistory" compareValue="true">
          T_Employee_SalaryHistory WITH(NOLOCK)
       </isEqual>
       <isEqual property="isHistory" compareValue="false">
             T_Employee_Salary WITH(NOLOCK)
       </isEqual>
        where salarytype ='工资' and company = '$company$'
        <isNotEqual property="userCode" prepend="and" compareValue="0">
          userCode = $userCode$
        </isNotEqual>
        <isNotEqual property="year" prepend="and" compareValue="0">
            year = $year$ and month = $month$
        </isNotEqual>
```  
