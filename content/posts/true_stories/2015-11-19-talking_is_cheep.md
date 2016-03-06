---
layout: post
title: "Talking is Cheap,show me the code"
modified:
categories: [truestories]
image: 25.jpg
tags: [truestories]
date: 2015-11-19T23:27:56
---

当看到如下的代码出现在production代码库的时候，不知道做何想法？无数的人动辄就谈客户需求，要触动痛点,是的没错，但是软件工程师还是要点工程追求的吧？如果这样的代码存在一些时候也就罢了，结果存在来Controller里面3-4年之久，情何以堪呀？指望用这样的代码去触动痛点？你是认真的吗？
工程师首先是个匠人,先写好自己的代码，再去谈论这些虚幻的东西.看几本抽象的书，谁都可以高谈阔论，so what? Talking is Cheap,right? show me the code.

```java
protected String formatUserJSON(VSalary newSalary){
		SimpleDateFormat sdf = new SimpleDateFormat("yyyy-MM-dd");
		String info = "{\"msg\":\""+Constants.SUCCESS+"\",\"usercode\":\""+newSalary.getUsercode()+"\",\"username\":\""+newSalary.getUsername()+"\"," +
				"\"orgname\":\""+newSalary.getOrgname()+"\",\"positionname\":\""+newSalary.getPositionname()+"\",\"hasexperience\":\""+newSalary.getHasexperience()+"\"," +
				"\"joindate\":\""+sdf.format(newSalary.getJoindate())+"\",\"leavedate\":\""+(newSalary.getLeavedate()==null?"":sdf.format(newSalary.getLeavedate()))+"\"," +
				"\"lastmonthwage\":\""+newSalary.getLastmonthwagestr()+"\",\"allowance\":\""+newSalary.getAllowancestr()+"\"," +
				"\"basewage\":\""+newSalary.getBasewagestr()+"\",\"totalwage\":\""+newSalary.getTotalwagestr()+"\"," +
				"\"transferdays\":\""+newSalary.getTransferdaysstr()+"\",\"paiddays\":\""+newSalary.getPaiddaysstr()+"\"," +
				"\"leavehours\":\""+newSalary.getLeavehoursstr()+"\",\"leavecost\":\""+newSalary.getLeavecoststr()+"\"," +
				"\"illdaystotal\":\""+newSalary.getIlldaystotalstr()+"\",\"illdays\":\""+newSalary.getIlldaysstr()+"\"," +
				"\"illcost\":\""+newSalary.getIllcoststr()+"\",\"latefreecount\":\""+newSalary.getLatefreecountstr()+"\"," +
				"\"latecostcount\":\""+newSalary.getLatecostcountstr()+"\",\"latecost\":\""+newSalary.getLatecoststr()+"\"," +
				"\"leaveearly\":\""+newSalary.getLeaveearlystr()+"\",\"leaveearlycost\":\""+newSalary.getLeaveearlycoststr()+"\"," +
				"\"missclockfreecount\":\""+newSalary.getMissclockfreecountstr()+"\",\"missclockcostcount\":\""+newSalary.getMissclockcostcountstr()+"\"," +
				"\"missclockcost\":\""+newSalary.getMissclockcoststr()+"\",\"absentcount\":\""+newSalary.getAbsentcountstr()+"\"," +
				"\"absentcost\":\""+newSalary.getAbsentcoststr()+"\",\"leavetotalcost\":\""+newSalary.getLeavetotalcoststr()+"\"," +
				"\"bussallowance\":\""+newSalary.getBussallowancestr()+"\",\"olderallowance\":\""+newSalary.getOlderallowancestr()+"\"," +
				"\"petrolallowance\":\""+newSalary.getPetrolallowancestr()+"\",\"otheradd\":\""+newSalary.getOtheraddstr()+"\"," +
				"\"otheraddremark\":\""+(newSalary.getOtheraddremark()==null?"":newSalary.getOtheraddremark())+"\",\"othertotal\":\""+newSalary.getOthertotalstr()+"\"," +
				"\"firededuction\":\""+newSalary.getFiredeductionstr()+"\",\"notfulldeduction\":\""+newSalary.getNotfulldeductionstr()+"\"," +
				"\"punishdeduction\":\""+newSalary.getPunishdeductionstr()+"\",\"otherdeduction\":\""+newSalary.getOtherdeductionstr()+"\"," +
				"\"otherdeductionremark\":\""+(newSalary.getOtherdeductionremark()==null?"":newSalary.getOtherdeductionremark())+"\",\"deductiontotal\":\""+newSalary.getDeductiontotalstr()+"\"," +
				"\"shouldtotal\":\""+newSalary.getShouldtotalstr()+"\",\"commission\":\""+newSalary.getCommissionstr()+"\",\"commissionDecu\":\""+newSalary.getCommissionDecustr()+"\",\"status\":\""+newSalary.getStatus()+"\","+
				"\"insuredtype\":\""+(newSalary.getInsuredtype()==null?"":newSalary.getInsuredtype())+"\",\"insuredbase\":\""+newSalary.getInsuredbasestr()+"\"," +
				"\"oldageinsurance\":\""+newSalary.getOldageinsurancestr()+"\",\"medicalinsurance\":\""+newSalary.getMedicalinsurancestr()+"\"," +
				"\"unemployedinsurance\":\""+newSalary.getUnemployedinsurancestr()+"\",\"accufundtype\":\""+(newSalary.getAccufundtype()==null?"":newSalary.getAccufundtype())+"\"," +
				"\"accufundbase\":\""+newSalary.getAccufundbasestr()+"\",\"accufund\":\""+newSalary.getAccufundstr()+"\"," +
				"\"socialinsurance\":\""+newSalary.getSocialinsurancestr()+"\",\"taxtotal\":\""+newSalary.getTaxtotalstr()+"\"," +
				"\"persontax\":\""+newSalary.getPersontaxstr()+"\",\"financialdeduction\":\""+newSalary.getFinancialdeductionstr()+"\"," +
				"\"finalwage\":\""+newSalary.getFinalwagestr()+"\",\"reward\":\""+ newSalary.getRewardstr()+ "\"," +
				"\"otherdeductionList\":"+JSONArray.fromObject(newSalary.getOtherdeductionList()).toString()+ "," +
				"\"negativeAmount\":\""+newSalary.getNegativeAmountstr()+"\"," +
				"\"currentsocialinsurance\":\""+newSalary.getCurrentsocialinsurancestr()+"\"," +
				"\"surplussocialinsurance\":\""+newSalary.getSurplussocialinsurancestr()+"\"," +
				"\"currentaccufund\":\""+newSalary.getCurrentaccufundstr()+"\"," +
				"\"surplusaccufund\":\""+newSalary.getSurplusaccufundstr()+"\"," +
				"\"currentoldageinsurance\":\""+newSalary.getCurrentoldageinsurancestr()+"\"," +
				"\"surplusoldageinsurance\":\""+newSalary.getSurplusoldageinsurancestr()+"\"," +
				"\"currentmedicalinsurance\":\""+newSalary.getCurrentmedicalinsurancestr()+"\"," +
				"\"surplusmedicalinsurance\":\""+newSalary.getSurplusmedicalinsurancestr()+"\"," +
				"\"currentunemployedinsurance\":\""+newSalary.getCurrentunemployedinsurancestr()+"\"," +
				"\"surplusunemployedinsurance\":\""+newSalary.getSurplusunemployedinsurancestr()+"\"," +
				"\"withholdingAdd\":\""+newSalary.getWithholdingAddstr()+"\"," +
				"\"withholdingDeduction\":\""+newSalary.getWithholdingDeductionstr()+"\"," +
				"\"withholdingAddRemark\":\""+(newSalary.getWithholdingAddRemark() == null ? "" : newSalary.getWithholdingAddRemark())+"\"," +
				"\"commissionDecRemark\":\""+(newSalary.getCommissionDecRemark() == null ? "" : newSalary.getCommissionDecRemark())+"\"," +
				"\"withholdingDeductionRemark\":\""+(newSalary.getWithholdingDeductionRemark() == null ? "" : newSalary.getWithholdingDeductionRemark())+"\"," +
				"\"currentwithholdingdeduction\":\""+newSalary.getCurrentwithholdingdeductionstr()+"\"," +
				"\"surpluswithholdingdeduction\":\""+newSalary.getSurpluswithholdingdeductionstr()+"\"," +
				"\"currentfinancialdeduction\":\""+newSalary.getCurrentfinancialdeductionstr()+"\"," +
				"\"partnerallowance\":\"" + newSalary.getPartnerallowancestr() + "\"}";
		return info;
	}
```

其实还有一些好玩的例子，不过没有这个极端而已。不过也可以来说说，可能是常见的不用心写出来的代码:

```java
m.put("totalCount", apiSalaryService.totalCount(pMap));
m.put("totalMoney", apiSalaryService.totalMoney(pMap));
m.put("payList",apiSalaryService.querySalaries(pMap));
m.put("isHistory",!SalaryHelper.isCurrent(year,month));
```
这样的开销真的好吗？

sql 如下， 我的疑问是难道totalCount，totalMoney不能用一个SQL取吗？或许list都取出来了，直接计算一下可能会更快，至少节省了
数据库服务器的资源. 数据库是最难水平扩展的资源.

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
        <isNotEqual property="userCode" prepend="and" compareValue="0">
            userCode = $userCode$
        </isNotEqual>
        <isNotEqual property="year" prepend="and" compareValue="0">
            year = $year$ and month = $month$
        </isNotEqual>
     </select>
</sqlMap>
```

## Another Duplicated DB Calls

```java
PropertyEntrustApply aEntrust = aService.selectPropertyEntrustApply(propertyId, IConst.EntrustType.A);
PropertyEntrustApply bEntrust = aService.selectPropertyEntrustApply(propertyId, IConst.EntrustType.B);
PropertyEntrustApply cRentEntrust = aService.selectPropertyEntrustApply(propertyId, IConst.EntrustType.C);
PropertyEntrustApply dSellEntrust = aService.selectPropertyEntrustApply(propertyId, IConst.EntrustType.D);
PropertyEntrustApply eEntrust = aService.selectPropertyEntrustApply(propertyId, IConst.EntrustType.E);

```

```java
public PropertyEntrustApply selectPropertyEntrustApply(String propertyId, EntrustType entrustType) {
			 List<PropertyEntrustApply> propertyEntrustApplyList = propertyEntrustApplyDao.listByPropertyId(propertyId);
			 for (PropertyEntrustApply propertyEntrustApply : propertyEntrustApplyList) {
					 if (entrustType.getValue().equals(propertyEntrustApply.getEntrustType())) {
							 return propertyEntrustApply;
					 }
			 }
			 return null;
	 }
```

问开发说这里5次数据库访问没有必要，开发说参数不同，需要的5次访问，其实测试也那么好糊弄，the code never lies.
然后再仔细一看说没时间改，其实改这个需用5分钟吗？
