```java
public List<Privilege> getPrivilegeByUserId(Integer companyId, int userCode, String appCode) {
        if(companyId == null) {
            companyId = Integer.valueOf(Company.Dooioo.companyIdentity());
        }

        String key = MemcachedHelper.getPriCacheKey(companyId.intValue(), userCode);

        try {
            if(this.plusOMSMemcachedClient.get(key) == null) {
                HashMap e = new HashMap();
                String[] map1 = appCode.split(",");
                e.put("userCode", Integer.valueOf(userCode));
                e.put("appCodes", map1);
                e.put("company", companyId);
                List appCodes1 = this.queryForList(e);
                this.plusOMSMemcachedClient.set(key, '\ua8c0', appCodes1);
                return appCodes1;
            } else {
                return (List)this.plusOMSMemcachedClient.get(key);
            }
        } catch (Exception var9) {
            HashMap map = new HashMap();
            String[] appCodes = appCode.split(",");
            map.put("userCode", Integer.valueOf(userCode));
            map.put("appCodes", appCodes);
            List pris = this.queryForList(map);
            return pris;
        }
    }
```
