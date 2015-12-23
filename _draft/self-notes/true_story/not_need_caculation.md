代码review的时候发下如下代码:

```java
	public List<Organization> findAllForegroundSubOrgs(Integer userCode,List<AllotDepartment> existOrgs) {
		List<Organization> orgs = queryDao.queryForList(sqlId("findAllForegroundSubOrgs"), userCode);
		List<Organization> needOrgs = new ArrayList<Organization>();
		Map<Integer,String> orgIds = new HashMap<Integer,String>();
		Map<String,Integer> orgNames = new HashMap<String,Integer>();
		//过滤已提交过的分行
		if (existOrgs != null){
			for (AllotDepartment org : existOrgs){
				orgIds.put(Integer.parseInt(org.getOrgId().toString()), org.getOrgName());
				orgNames.put(org.getOrgName(), org.getId());
			}
		}
		for (Organization org : orgs){
			if (orgIds.containsKey(org.getId())){
				org.setOpenDate(new Date());
			} else if (!orgNames.containsKey(org.getOrgName())){
				needOrgs.add(org);
				orgNames.put(org.getOrgName(),org.getId());
			}
		}
		return needOrgs;
	}
```

问题1：
- if exitOrgs is null,looks no need to add any needOrds,basically need to check existingOrgs size first

```java
node.setAssignee(employee.getUserCode()+"");
```
