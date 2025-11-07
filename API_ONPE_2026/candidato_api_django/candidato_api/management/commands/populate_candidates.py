# candidato_api/management/commands/populate_candidates.py

from django.core.management.base import BaseCommand
from candidato_api.models import Candidate
import json

class Command(BaseCommand):
    help = 'Pobla la base de datos con datos de candidatos'

    def handle(self, *args, **options):
        # Limpiar datos anteriores
        Candidate.objects.all().delete()
        
        candidates_data = [
            # --- CANDIDATO 1: Rafael López Aliaga ---
            {
                "id": 1,
                "name": "Rafael López Aliaga",
                "party": "Renovación Popular",
                "position": "Presidencia",
                "photo_url": "https://tse1.mm.bing.net/th/id/OIP.aAFAdIKomuFf5FSyxibhMQHaHa?rs=1&pid=ImgDetMain&o=7&rm=3",
                "basic_info": {
                    "birthDate": "11/02/1961",
                    "birthPlace": "Lima",
                    "age": "64 años",
                    "maritalStatus": "Soltero",
                    "residence": "Lima"
                },
                "asset_declaration": {
                    "totalValue": 2500000.0,
                    "assets": [
                        {"name": "Inmuebles", "value": 1800000.0, "color": "#E53935"},
                        {"name": "Vehículos", "value": 300000.0, "color": "#3C3472"},
                        {"name": "Ingresos anuales (último)", "value": 400000.0, "color": "#6E6E6E"}
                    ]
                },
                "government_plan": {
                    "summary": "Plan de gobierno centrado en la inversión privada, seguridad ciudadana y programas sociales directos.",
                    "proposals": [
                        {"title": "Economía", "description": "Fomento de la inversión y reducción de la burocracia para la creación de 2 millones de empleos."},
                        {"title": "Seguridad", "description": "Implementación de sistema de 'policía de barrio' y tecnología de vigilancia avanzada."},
                        {"title": "Social", "description": "Lanzamiento del 'Plan Cero Hambre' enfocado en la lucha contra la desnutrición infantil."}
                    ],
                    "document_id": "plan_gobierno_1",
                    "document_url": "https://declara.jne.gob.pe/ASSETS/PLANGOBIERNO/FILEPLANGOBIERNO/16482.pdf"
                },
                "academic_formation": {
                    "degrees": [
                        {"title": "Maestría en Administración de Empresas (MBA)", "institution": "Universidad de Piura (1990-1992)"},
                        {"title": "Ingeniería Industrial", "institution": "Universidad Nacional de Ingeniería (UNI) (1979-1984)"},
                        {"title": "Programa de Alta Dirección (PAD)", "institution": "IESE Business School, Barcelona"}
                    ],
                    "sunedu_id": "sunedu_1"
                },
                "career_history": {
                    "items": [
                        {"position": "Alcalde Metropolitano de Lima", "period": "2023-Presente", "description": "Gestión municipal enfocada en seguridad, transporte y programas sociales. Liderazgo en el sector público."},
                        {"position": "Presidente del Directorio", "period": "Grupo PeruRail (1999-2022)", "description": "Liderazgo y gestión en el sector ferroviario y turismo. Expansión de rutas y servicios."},
                        {"position": "Gerente General", "period": "Banco de Comercio (1995-1999)", "description": "Responsable de la dirección estratégica y operativa del banco."}
                    ]
                },
                "background_report": {
                    "records": [
                        {
                            "title": "Investigación por Lavado de Activos",
                            "entity": "Ministerio Público (Fiscalía de la Nación)",
                            "date": "15/05/2021",
                            "description": "Investigación preliminar en el marco del caso 'Panama Papers' por presuntos aportes no justificados. El caso está en etapa de indagación.",
                            "statusTags": ["Activo", "Investigación Preliminar"],
                            "classificationTags": ["Lavado de Activos", "Finanzas"],
                            "documentId": "doc_antecedente_1_1"
                        },
                        {
                            "title": "Proceso Administrativo por Deudas Tributarias",
                            "entity": "Superintendencia Nacional de Aduanas y de Administración Tributaria (SUNAT)",
                            "date": "01/03/2019",
                            "description": "Deuda tributaria de una de sus empresas, actualmente en proceso de fraccionamiento y pago.",
                            "statusTags": ["En Proceso de Pago", "Administrativo"],
                            "classificationTags": ["Tributario", "Finanzas"],
                            "documentId": "doc_antecedente_1_2"
                        }
                    ]
                },
                "current_events": {
                    "items": [
                        {
                            "id": 101,
                            "type": "noticia",
                            "title": "Rafael López Aliaga si cumple con ollitas comunes",
                            "description": "A través de una conferencia de prensa se detalló el trabajo que se realiza desde la MML.",
                            "date": "2023-10-31",
                            "source": "MML",
                            "relatedTo": "Rafael López Aliaga",
                            "isVerified": "true",
                            "documentId": "doc_noticia_101"
                        },
                        {
                            "id": 102,
                            "type": "actividad",
                            "title": "Mitin de cierre en Plaza San Martín",
                            "description": "Realizó un evento masivo en el centro de Lima.",
                            "date": "2025-10-14",
                            "source": "RPP Noticias",
                            "relatedTo": "Rafael López Aliaga",
                            "isVerified": "false",
                            "documentId": "doc_actividad_102"
                        }
                    ]
                }
            },
            # --- CANDIDATO 2: Keiko Fujimori ---
            {
                "id": 2,
                "name": "Keiko Fujimori",
                "party": "Fuerza Popular",
                "position": "Presidencia",
                "photo_url": "https://tvperu.gob.pe/sites/default/files/000778186w.jpg",
                "basic_info": {
                    "birthDate": "25/05/1975",
                    "birthPlace": "Lima",
                    "age": "50 años",
                    "maritalStatus": "Casada",
                    "residence": "Lima"
                },
                "asset_declaration": {
                    "totalValue": 1100000.0,
                    "assets": [
                        {"name": "Bienes Inmuebles", "value": 550000.0, "color": "#388E3C"},
                        {"name": "Cuentas Bancarias", "value": 550000.0, "color": "#00796B"}
                    ]
                },
                "government_plan": {
                    "summary": "Propuesta de reactivación económica y reforma política.",
                    "proposals": [
                        {"title": "Reforma Judicial", "description": "Creación de una comisión de alto nivel para depurar el sistema de justicia."},
                        {"title": "Economía", "description": "Incentivos fiscales para la inversión en regiones."}
                    ],
                    "document_id": "plan_gobierno_2",
                    "document_url": "https://apisije-e.jne.gob.pe/TRAMITE/ESCRITO/1095/ARCHIVO/FIRMADO/3017.PDF"
                },
                "academic_formation": {
                    "degrees": [
                        {"title": "Maestría en Administración de Negocios (MBA)", "institution": "Columbia University (2000-2002)"},
                        {"title": "Bachiller en Administración de Empresas", "institution": "Boston University (1993-1997)"}
                    ],
                    "sunedu_id": "sunedu_2"
                },
                "career_history": {
                    "items": [
                        {"position": "Congresista de la República", "period": "2006-2011", "description": "Representante por Lima. Presidenta de la Comisión de Fiscalización."}
                    ]
                },
                "background_report": {
                    "records": [
                         {
                        "title": "Investigación por Aportes de Campaña",
                        "entity": "Ministerio Público",
                        "date": "20/09/2018",
                        "description": "Investigación por presuntos aportes ilícitos a la campaña presidencial de 2011 y 2016 (Caso Cócteles).",
                        "statusTags": ["Activo", "Investigación Formalizada"],
                        "classificationTags": ["Crimen Organizado", "Financiamiento Ilegal"],
                        "documentId": "doc_antecedente_2_1"
                         }                    
                    ]
                },
                "current_events": {
                    "items": [
                        {
                            "id": 201,
                            "type": "noticia",
                            "title": "Fujimori presenta plan de gobierno enfocado en reactivacion economica",
                            "description": "La candidata detalló su plan de reactivación económica.",
                            "date": "2025-10-18",
                            "source": "El Comercio",
                            "relatedTo": "Keiko Fujimori",
                            "isVerified": "true",
                            "documentId": "doc_noticia_201"
                        },
                        {
                            "id": 203,
                            "type": "documento",
                            "title": "Fuerza Popular publica versión final de plan de gobierno",
                            "description": "El partido publicó la versión consolidada del plan de gobierno ante el JNE.",
                            "date": "2025-09-21",
                            "source": "JNE",
                            "relatedTo": "Keiko Fujimori",
                            "isVerified": "true",
                            "documentId": "doc_documento_203"
                        }
                    ]
                }

            },
            # --- CANDIDATO 3: César Acuña ---
            {
                "id": 3,
                "name": "César Acuña",
                "party": "Alianza para el Progreso",
                "position": "Presidencia",
                "photo_url": "https://portal.andina.pe/EDPfotografia3/Thumbnail/2021/03/29/000761739W.jpg",
                "basic_info": {
                    "birthDate": "11/08/1952",
                    "birthPlace": "Cajamarca",
                    "age": "73 años",
                    "maritalStatus": "Casado",
                    "residence": "Lima"
                },
                "asset_declaration": {
                    "totalValue": 5000000.0,
                    "assets": [
                        {"name": "Empresas y Acciones", "value": 3500000.0, "color": "#FFC107"},
                        {"name": "Inmuebles", "value": 1500000.0, "color": "#FF9800"}
                    ]
                },
                "government_plan": {
                    "summary": "Énfasis en la educación y descentralización del país.",
                    "proposals": [
                        {"title": "Educación", "description": "Inversión del 6% del PBI y creación de universidades tecnológicas en cada región."},
                        {"title": "Descentralización", "description": "Mayor autonomía a gobiernos regionales y locales."}
                    ],
                    "document_id": "plan_gobierno_3",
                    "document_url": "https://mpesije.jne.gob.pe/docs/1632dad2-4408-461c-b5e0-ba87a0c19027.pdf"
                },
                "academic_formation": {
                    "degrees": [
                        {"title": "Doctor en Educación", "institution": "Universidad Complutense de Madrid"},
                        {"title": "Maestría en Dirección Universitaria", "institution": "Universidad de Los Andes"}
                    ],
                    "sunedu_id": "sunedu_3"
                },
                "career_history": {
                    "items": [
                        {"position": "Gobernador Regional de La Libertad", "period": "2019-Presente", "description": "Gestión regional con enfoque en infraestructura y salud."},
                        {"position": "Alcalde de Trujillo", "period": "1999-2006", "description": "Dos periodos de gestión municipal en Trujillo."}
                    ]
                },
                "background_report": {
                    "records": [
                        {
                            "title": "Denuncia por Plagio",
                            "entity": "Comisión de Ética del Congreso",
                            "date": "20/01/2016",
                            "description": "Acusación por plagio en tesis doctoral y otros trabajos académicos. Generó polémica pública.",
                            "statusTags": ["Cerrado", "Polémico"],
                            "classificationTags": ["Ética", "Académico"],
                            "documentId": "doc_antecedente_3_1"
                        }
                    ]
                },
                "current_events": {
                    "items": [
                        {
                            "id": 301,
                            "type": "noticia",
                            "title": "Acuña promete 'Educación como Revolución'",
                            "description": "El candidato de APP centró su discurso en la inversión del 6% del PBI para el sector educativo.",
                            "date": "2025-10-17",
                            "source": "La República",
                            "relatedTo": "César Acuña",
                            "isVerified": "false",
                            "documentId": "doc_noticia_301"
                        }
                    ]
                }

            },
            # --- CANDIDATO 5: Martín Vizcarra ---
            {
                "id": 5,
                "name": "Martín Vizcarra",
                "party": "Perú Primero",
                "position": "Presidencia",
                "photo_url": "https://tse2.mm.bing.net/th/id/OIP.rEIcUIfKg887VmAIBBNYLwHaE8?rs=1&pid=ImgDetMain&o=7&rm=3",
                "basic_info": {
                    "birthDate": "22/03/1963",
                    "birthPlace": "Moquegua",
                    "age": "62 años",
                    "maritalStatus": "Casado",
                    "residence": "Moquegua"
                },
                "asset_declaration": {
                    "totalValue": 900000.0,
                    "assets": [
                        {"name": "Inmuebles", "value": 700000.0, "color": "#03A9F4"},
                        {"name": "Cuentas Bancarias", "value": 200000.0, "color": "#00BCD4"}
                    ]
                },
                "government_plan": {
                    "summary": "Reforma del sistema político y lucha contra la corrupción.",
                    "proposals": [
                        {"title": "Política", "description": "Reforma constitucional para limitar la inmunidad parlamentaria."},
                        {"title": "Salud", "description": "Fortalecimiento del sistema de salud pública post-pandemia."}
                    ],
                    "document_id": "plan_gobierno_5",
                    "document_url": "https://apisije-e.jne.gob.pe/TRAMITE/ESCRITO/1859/ARCHIVO/FIRMADO/7346.PDF"
                },
                "academic_formation": {
                    "degrees": [
                        {"title": "Ingeniería Civil", "institution": "Universidad Nacional de Ingeniería (UNI) (1981-1986)"}
                    ],
                    "sunedu_id": "sunedu_5"
                },
                "career_history": {
                    "items": [
                        {"position": "Presidente de la República", "period": "2018-2020", "description": "Gobierno enfocado en la lucha anticorrupción y reforma política."},
                        {"position": "Ministro de Transportes y Comunicaciones", "period": "2016-2017", "description": "Gestión de proyectos de infraestructura a nivel nacional."}
                    ]
                },
                "background_report": {
                    "records": [
                        {
                            "title": "Inhabilitación Política",
                            "entity": "Congreso de la República",
                            "date": "16/04/2021",
                            "description": "Inhabilitado por 10 años para ejercer cargos públicos por el caso 'Vacunagate' (vacunación irregular).",
                            "statusTags": ["Inhabilitado", "Sanción"],
                            "classificationTags": ["Corrupción", "Función Pública"],
                            "documentId": "doc_antecedente_5_1"
                        }
                    ]
                },
                "current_events": {
                    "items": [
                        {
                            "id": 501,
                            "type": "actividad",
                            "title": "Vizcarra apela inhabilitación ante TC",
                            "description": "Defensa legal del candidato presentó un recurso ante el Tribunal Constitucional.",
                            "date": "2025-10-10",
                            "source": "Canal N",
                            "relatedTo": "Martín Vizcarra",
                            "isVerified": "true",
                            "documentId": "doc_actividad_501"
                        }
                    ]
                }
            }
        ]
        
        for data in candidates_data:
            Candidate.objects.create(
                id=data['id'],
                name=data['name'],
                party=data['party'],
                position=data['position'],
                photo_url=data['photo_url'],
                basic_info=data['basic_info'],
                asset_declaration=data['asset_declaration'],
                government_plan=data['government_plan'],
                academic_formation=data['academic_formation'],
                career_history=data['career_history'],
                background_report=data['background_report'],
                current_events=data['current_events']
            )
        
        self.stdout.write(self.style.SUCCESS('✅ Base de datos poblada exitosamente con 4 candidatos'))
