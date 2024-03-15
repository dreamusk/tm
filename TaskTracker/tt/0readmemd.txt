Table Team {
  id int [primary key]
  name varchar(255)
}

Table Employee {
  empid varchar(255) [ref: > Work.empid]
  employee varchar(255) [primary key]
}

Table Work {
  id int [ref:>Team.id]
  empid varchar(255) [primary key]
}

Table Project {
  pid varchar(255) [primary key]
  pname varchar(255)
  abbreviation varchar(255)
}

Table Management {
  // id int [primary key]
  pno int [primary key]
  work_id int [ref: > Project.pid]
  empid varchar(255) [ref: > Work.empid]
}
