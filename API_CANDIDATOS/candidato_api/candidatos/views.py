from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['GET'])
def lista_candidatos(request):
    candidatos = [
        {
            "id": 1,
            "nombre": "Rafael López Aliaga",
            "partido": "Renovación Popular",
            "cargo": "Presidencia",
            "foto": "https://tse1.mm.bing.net/th/id/OIP.aAFAdIKomuFf5FSyxibhMQHaHa",
            "propuestas": [
                {"area": "Economía", "detalle": "Fomento de la inversión privada"},
                {"area": "Seguridad", "detalle": "Implementación de 'policía de barrio'"},
                {"area": "Social", "detalle": "Plan Cero Hambre"},
            ]
        },
        {
            "id": 2,
            "nombre": "Keiko Fujimori",
            "partido": "Fuerza Popular",
            "cargo": "Presidencia",
            "foto": "https://tvperu.gob.pe/sites/default/files/000778186w.jpg",
            "propuestas": [
                {"area": "Reforma Judicial", "detalle": "Depuración del sistema de justicia"},
                {"area": "Economía", "detalle": "Incentivos fiscales regionales"},
            ]
        },
        {
            "id": 3,
            "nombre": "César Acuña",
            "partido": "Alianza para el Progreso",
            "cargo": "Presidencia",
            "foto": "https://portal.andina.pe/EDPfotografia3/Thumbnail/2021/03/29/000761739W.jpg",
            "propuestas": [
                {"area": "Educación", "detalle": "Inversión del 6% del PBI"},
                {"area": "Descentralización", "detalle": "Autonomía regional"},
            ]
        }
    ]
    return Response(candidatos)
