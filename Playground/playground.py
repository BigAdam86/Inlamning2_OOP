import unittest

from person import Person
from staff import Staff
from student import Student

class TestPerson(unittest.TestCase):
    def test_person_01_constructor( self ):
        p = Person("Mark", "Min Gata 1")
        self.assertEqual( str(p), "Person[name=Mark,address=Min Gata 1]" )
"""
    def test_person_02_get_name( self ):
        p = Person("Mark", "Min Gata 1")
        self.assertEqual( p.getName(), "Mark" )

    def test_person_03_get_address( self ):
        p = Person("Mark", "Min Gata 1")
        self.assertEqual( p.getAddress(), "Min Gata 1" )

    def test_person_04_set_address( self ):
        p = Person("Mark", "Min Gata 1")
        p.setAddress( "Annan Gata 2" )
        self.assertEqual( p.getAddress(), "Annan Gata 2" )
    """