import pytest
from docx.document import Document as DocumentClass
import cv_generator


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
