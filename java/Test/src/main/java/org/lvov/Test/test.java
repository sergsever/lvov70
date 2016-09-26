package org.lvov.Test;
import org.springframework.context.ApplicationContext;
import org.springframework.context.support.ClassPathXmlApplicationContext;
import org.hibernate.cfg.Configuration;
import org.hibernate.Session;
import org.hibernate.SessionFactory;
import org.lvov.Test.Htest;
class Test {
private SessionFactory sessionfactory;
public static void main(String[] args) {
/*System.out.println("Before beans.\n");*/
System.out.println("Bean:" + get_from_bean());
}
public String get_from_db()
{
/*Configuration config = new Configuration().configure("hibernate.cfg.xml");
return "";*/
//var config  = new Configuration().configure();
//config.CurrentSessionContext<WebSessionContext>();
Session session = new Configuration().configure().buildSessionFactory().getCurrentSession();
Htest t = (Htest)session.get(Htest.class, new Integer(1)); 
return t.get_name();

} 
public static String get_from_bean()
{
 ApplicationContext context = new ClassPathXmlApplicationContext("Beans.xml");
TBean tbean = (TBean) context.getBean("TBean");
return tbean.getMessage();
}
}
