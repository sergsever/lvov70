package org.lvov.Test;

import javax.persistence.*;
import javax.persistence.Entity;

@Entity
@Table(name="htest")
public class Htest {
@Id
@GeneratedValue(strategy = GenerationType.AUTO, generator = "my_entity_seq_gen")
@SequenceGenerator(name = "my_entity_seq_gen", sequenceName = "catalog_seq")private long id;
@Column
private String name;
public String get_name()
{
return name;
}
}
