import os
import sys
import pytest
from docx.document import Document as DocumentClass
import cv_generator

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

def test_load_cv_content_returns_dict():
    content = cv_generator.load_cv_content('cv_content.json')
    assert isinstance(content, dict)


def test_create_cv_returns_document_instance():
    content = cv_generator.load_cv_content('cv_content.json')
    doc = cv_generator.create_cv(content)
    assert isinstance(doc, DocumentClass)
    # Verify that at least the 'Professional Summary' heading is present
    texts = [p.text for p in doc.paragraphs]
    assert 'Professional Summary' in texts

