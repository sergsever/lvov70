package org.lvov.Test;

import junit.framework.Test;
import junit.framework.TestCase;
import junit.framework.TestSuite;

/**
 * Unit test for simple App.
 */
public class AppTest
    extends TestCase
{
    /**
     * Create the test case
     *
     * @param testName name of the test case
     */
    public AppTest( String testName )
    {
        super( testName );
    }

    /**
     * @return the suite of tests being tested
     */
    public static Test suite()
    {
        return new TestSuite( AppTest.class );
    }

    /**
     * Rigourous Test :-)
     */
    public void testApp()
    {
	System.out.println( org.lvov.Test.Test.get_from_bean());
        assertTrue(org.lvov.Test.Test.get_from_bean().equals("Hello!"));
	org.lvov.Test.Test test = new org.lvov.Test.Test();

	String hib_res = test.get_from_db(); 
    }
}
