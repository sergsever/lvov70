package org.lvov.Test;
import org.springframework.context.ApplicationContext;
import org.springframework.context.support.ClassPathXmlApplicationContext;
class Test {
public static void main(String[] args) {
/*System.out.println("Before beans.\n");*/
System.out.println("Bean:" + get_from_bean());
}
public static String get_from_bean()
{
 ApplicationContext context = new ClassPathXmlApplicationContext("Beans.xml");
TBean tbean = (TBean) context.getBean("TBean");
return tbean.getMessage();
}
}
