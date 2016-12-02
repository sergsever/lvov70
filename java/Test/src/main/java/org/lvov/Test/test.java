package org.lvov.Test;
import org.springframework.context.ApplicationContext;
import org.springframework.context.support.ClassPathXmlApplicationContext;
import org.hibernate.cfg.Configuration;
import org.hibernate.Session;
import org.hibernate.SessionFactory;
import org.lvov.Test.Htest;
import org.hibernate.Transaction;
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
String result;
Configuration conf = new Configuration().configure();
	conf.addAnnotatedClass(Htest.class);
Session session = conf.buildSessionFactory().getCurrentSession();
Transaction tx = session.beginTransaction(); 
Htest t = (Htest)session.get(Htest.class, new Long(1)); 
result = t.get_name();
tx.commit();
System.out.println("result:" + result);
return result;

} 
public static String get_from_bean()
{
 ApplicationContext context = new ClassPathXmlApplicationContext("Beans.xml");
TBean tbean = (TBean) context.getBean("TBean");
return tbean.getMessage();
}
}
