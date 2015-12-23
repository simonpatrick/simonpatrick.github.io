# Idea Plugin 开发
以下是如何开发plugin的

## 步骤
- creating new plugin module
- creating an action
- registering actions

## idea plugin基本概念
- general threading rules
- virtual files
- Documents
- PSI Files
- File View Providers
- PSI Elements

## Plugin Structure
- Plugin content
- plugin class loaders
- plugin components
- plugin extensions and extensions points
- plugin actions
- plugin services
- plugin configuration files
- plugin Dependencies

### plugin  content

- jar file 在Plugin的目录下面 //todo add picture
- plugin 文件在plugin的应用目录下面
- Plugin里面的JAR包在应用目录下面的Lib目录

### Plugin class loader
IDEA使用单独的class loader，每一个插件都可能不同。
class loader可以在plugin.xml里面配置,可以依赖其他插件

### plugin component
plugin component是插件的基础概念，idea里面有三层不同的组件：

- application-level

application level的类在idea启动时就加载，可以通过```getComponent()```获得

- project-level

每个项目都会建立一个实例，通过project层的```getComponent()```获得实例

- module-level

```
	Module-level components are created for each Module in every project loaded in IDEA. Module-level component can be acquired from Module instance with the same method.

	Every component should have interface and implementation classes specified in the configuration file. The interface class will be used for retrieving the component from other components and the implementation class will be used for component instantiation. Note that two components of the same level (Application, Project or Module) cannot have the same interface class. Interface and implementation classes can be the same.
	Each component has the unique name which is used for its externalization and other internal needs. The name of a component is returned by its getComponentName() method.


```

#### Persisting State of Components

```
	The state of every component will be automatically saved and loaded if the component's class implements the JDOMExternalizable (deprecated) or PersistentStateComponent interface.

	When the component's class implements the PersistentStateComponent interface, the component state is saved in an XML file that you can specify using the @State and @Storage annotations in your Java code.

	When the component's class implements the JDOMExternalizable interface, the components save their state in the following files:

	Project-level components save their state to the project (.ipr) file. However, if the workspace option in the plugin.xml file is set to true, the component saves its configuration to the workspace (.iws) file instead.
	Module-level components save their state to the module (.iml) file.
	For more information and samples, refer to Persisting State of Components.
```

### Plugin Components Lifecycle

```
The components are loaded in the following order:

Creation - constructor is invoked.
Initialization - the initComponent method is invoked (if the component implements the ApplicationComponent interface).
Configuration - the readExternal method is invoked (if the component implements JDOMExternalizable interface), or the loadState method is invoked (if the component implements PersistentStateComponent and has non-default persisted state).
For module components, the moduleAdded method of the ModuleComponent interface is invoked to notify that a module has been added to the project.
For project components, the projectOpened method of the ProjectComponent interface is invoked to notify that a project has been loaded.

The components are unloaded in the following order:

Saving configuration - the writeExternal method is invoked (if the component implements the JDOMExternalizable interface), or the getState method is invoked (if the component implements PersistentStateComponent).
Disposal - the disposeComponent method is invoked.
```

### Plugin Extensions and Extension Points
Intellij IDEA provides the concept of extensions and extension points that allows a plugin to interact with other plugins or with the IDEA core.

```
	How to Get the Extension Points List?
	To get a list of extension points available in the IntelliJ IDEA core, consult the <extensionPoints> section of the following XML configuration files:

	LangExtensionPoints.xml
	PlatformExtensionPoints.xml
	VcsExtensionPoints.xml
```


### Plugin Actions
Intellij IDEA provides the concept of actions. An action is a class, derived from the AnAction class, whose actionPerformed method is called when the menu item or toolbar button is selected. The system of actions allows plugins to add their own items to IDEA menus and toolbars.
Actions are organized into groups, which, in turn, can contain other groups. A group of actions can form a toolbar or a menu. Subgroups of the group can form submenus of the menu.
You can find detailed information on how to create and register your actions in IntelliJ IDEA Action System and in Creating an Action .

### Plugin Services
IntelliJ IDEA provides the concept of services. A service is a plugin component loaded on demand, when your plugin calls the getService method of the ServiceManager class. IntelliJ IDEA ensures that only one instance of a service is loaded even though the service is called several times. A service must have the interface and implementation classes specified in the plugin.xml file. 
The service implementation class is used for service instantiation.
IntelliJ IDEA offers three types of services: application level services, project level services and module level services.

#### How to Declare a Service?
To declare a service, you can use the following extension points in the IDEA core:

applicationService: designed to declare an application level service.
projectService: designed to declare a project level service.
moduleService: designed to declare a module level service.
To declare a service

Add the appropriate child element (<applicationService>, <projectService> or <moduleService>) to the <extensions> section of the plugin.xml file.
For the newly added child element, set the following attributes:
serviceInterface: specifies the service interface class.
serviceImplementation: specifies the service implementation class.

### Plugin Dependencies

```
<depends>other.plugin</depends>
```

### Register Actions

- plugin.xml
- code

sample codes:

```xml
	<!-- Actions -->
    <actions>
        <!-- The <action> element defines an action to register.
               The mandatory "id" attribute specifies an unique identifier for the action.
               The mandatory "class" attribute specifies the full-qualified name of the class implementing the action.
               The mandatory "text" attribute specifies the text of the action (tooltip for toolbar button or text for menu item).
              The optional "use-shortcut-of" attribute specifies the ID of the action whose keyboard shortcut this action will use.  
              The optional "description" attribute specifies the text which is displayed in the status bar when the action is focused.
               The optional "icon" attribute specifies the icon which is displayed on the toolbar button or next to the menu item. -->
        <action id="VssIntegration.GarbageCollection" class="com.foo.impl.CollectGarbage" text="Collect _Garbage" description="Run garbage collector"
                icon="icons/garbage.png">
             <!-- The <add-to-group> node specifies that the action should be added to an existing group. An action can be added to several groups.
                    The mandatory "group-id" attribute specifies the ID of the group to which the action is added.
                    The group must be implemented by an instance of the DefaultActionGroup class.
                    The mandatory "anchor" attribute specifies the position of the action in the group relative to other actions. It can have the values
                    "first", "last", "before" and "after".
                    The "relative-to-action" attribute is mandatory if the anchor is set to "before" and "after", and specifies the action before or after which
                    the current action is inserted. -->
            <add-to-group group-id="ToolsMenu" relative-to-action="GenerateJavadoc" anchor="after"/>
             <!-- The <keyboard-shortcut> node specifies the keyboard shortcut for the action. An action can have several keyboard shortcuts.
                    The mandatory "first-keystroke" attribute specifies the first keystroke of the action. The key strokes are specified according to the regular Swing rules.
                    The optional "second-keystroke" attribute specifies the second keystroke of the action.
                    The mandatory "keymap" attribute specifies the keymap for which the action is active. IDs of the standard keymaps are defined as
                    constants in the com.intellij.openapi.keymap.KeymapManager class. -->
            <keyboard-shortcut first-keystroke="control alt G" second-keystroke="C" keymap="$default"/>
             <!-- The <mouse-shortcut> node specifies the mouse shortcut for the action. An action can have several mouse shortcuts.
                    The mandatory "keystroke" attribute specifies the clicks and modifiers for the action. It is defined as a sequence of words separated by spaces:
                    "button1", "button2", "button3" for the mouse buttons; "shift", "control", "meta", "alt", "altGraph" for the modifier keys;
                    "doubleClick" if the action is activated by a double-click of the button.
                    The mandatory "keymap" attribute specifies the keymap for which the action is active. IDs of the standard keymaps are defined as
                    constants in the com.intellij.openapi.keymap.KeymapManager class. -->
            <mouse-shortcut keystroke="control button3 doubleClick" keymap="$default"/>
        </action>
        <!-- The <group> element defines an action group. <action>, <group> and <separator> elements defined within it are automatically included in the group.
               The mandatory "id" attribute specifies an unique identifier for the action.
               The optional "class" attribute specifies the full-qualified name of the class implementing the group. If not specified,
               com.intellij.openapi.actionSystem.DefaultActionGroup is used.
               The optional "text" attribute specifies the text of the group (text for the menu item showing the submenu).
               The optional "description" attribute specifies the text which is displayed in the status bar when the group is focused.
               The optional "icon" attribute specifies the icon which is displayed on the toolbar button or next to the group.
               The optional "popup" attribute specifies how the group is presented in the menu. If a group has popup="true", actions in it
               are placed in a submenu; for popup="false", actions are displayed as a section of the same menu delimited by separators. -->
        <group class="com.foo.impl.MyActionGroup" id="TestActionGroup" text="Test Group" description="Group with test actions"
               icon="icons/testgroup.png" popup="true">
            <action id="VssIntegration.TestAction" class="com.foo.impl.TestAction" text="My Test Action" description="My test action"/>
            <!-- The <separator> element defines a separator between actions. It can also have an <add-to-group> child element. -->
            <separator/>
            <group id="TestActionSubGroup"/>
             <!-- The <reference> element allows to add an existing action to the group. The mandatory "ref" attribute specifies the ID of the action to add. -->
            <reference ref="EditorCopy"/>
            <add-to-group group-id="MainMenu" relative-to-action="HelpMenu" anchor="before"/>
        </group>
    </actions>
```

代码注册： 

```java
	public class MyPluginRegistration implements ApplicationComponent {
  // Returns the component name (any unique string value).    
    @NotNull public String getComponentName() {
        return "MyPlugin";                
    }
 
 
// If you register the MyPluginRegistration class in the <application-components> section of 
// the plugin.xml file, this method is called on IDEA start-up.
    public void initComponent() {
        ActionManager am = ActionManager.getInstance();
        TextBoxes action = new TextBoxes();
      // Passes an instance of your custom TextBoxes class to the registerAction method of the ActionManager class. 
        am.registerAction("MyPluginAction", action);
      // Gets an instance of the WindowMenu action group.
        DefaultActionGroup windowM = (DefaultActionGroup) am.getAction("WindowMenu");
      // Adds a separator and a new menu command to the WindowMenu group on the main menu.  
        windowM.addSeparator();
        windowM.add(action);
    }
 
// Disposes system resources.
    public void disposeComponent() {        
    }
}
```