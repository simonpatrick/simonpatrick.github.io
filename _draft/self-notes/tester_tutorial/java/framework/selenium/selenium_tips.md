# selenium tips

## Turn off firefox alert

```java
user_pref("capability.policy.policynames", "strict");
user_pref("capability.policy.strict.sites", "yourdomain.com");
user_pref("capability.policy.strict.Window.alert", "noAccess");
user_pref("capability.policy.strict.Window.confirm", "noAccess");
user_pref("capability.policy.strict.Window.prompt", "noAccess");
```