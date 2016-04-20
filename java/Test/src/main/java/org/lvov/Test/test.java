package org.lvov.Test;
import org.springframework.context.ApplicationContext;
import org.springframework.context.support.ClassPathXmlApplicationContext;
class Test {
public static void main(String[] args) {
/*System.out.println("Before beans.\n");*/
ApplicationContext context = new ClassPathXmlApplicationContext("Beans.xml");
TBean tbean = (TBean) context.getBean("TBean");
System.out.println(tbean.getMessage());
}
}
