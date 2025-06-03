import os
import sys
import pytest

sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))
from cv_generator import create_cv

def minimal_content():
    return {
        'personal_info': {'name': 'Name', 'contact': 'Contact'},
        'professional_summary': 'Summary.',
        'key_skills': ['Skill1', 'Skill2'],
        'accomplishments': [],
        'work_history': [],
        'education': [],
        'certifications': []
    }

def test_key_skills_section_present():
    doc = create_cv(minimal_content())
    texts = [p.text for p in doc.paragraphs]
    assert 'Key Skills' in texts
    index = texts.index('Key Skills')
    assert texts[index + 1] == 'Skill1'
    assert texts[index + 2] == 'Skill2'
    assert doc.paragraphs[index].style.name == 'CustomHeading'
    assert doc.paragraphs[index + 1].style.name == 'List Bullet'
