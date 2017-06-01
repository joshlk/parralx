
from google.cloud import vision
from google.cloud.vision.feature import Feature

vision_client = vision.Client(project="parralx")

def plarralx_verifiy(image_url):
    image = vision_client.image(source_uri=image_url)
    
    res = image.detect([Feature('LABEL_DETECTION'), Feature('LOGO_DETECTION'), Feature('SAFE_SEARCH_DETECTION')])
    r = res[0]
    
    # Logos
    logos = [logo.description for logo in r.logos]
    
    # Safe search
    safe_search = r.safe_searches
    adult = safe_search.adult.name
    violence = safe_search.violence.name
    
    # Labels
    labels = [label.description for label in r.labels]
    
    output = {
        'inappropriate_content': {
            'contains_logos': logos,
            'contains_adult': adult,
            'contains_violence': violence
        },
        
        'content_labels': labels
    }
    
    return output