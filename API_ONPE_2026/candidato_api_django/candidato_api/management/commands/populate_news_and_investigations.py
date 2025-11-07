from django.core.management.base import BaseCommand
from candidato_api.models import NewsDetail, InvestigationDetail

class Command(BaseCommand):
    help = "Pobla la base de datos con detalles de noticias e investigaciones"

    def handle(self, *args, **options):
        NewsDetail.objects.all().delete()
        InvestigationDetail.objects.all().delete()

        # Noticias
        news_data = [
        # Rafael López Aliaga (RLA)
        {
            "document_id": "doc_noticia_101",
            "title": "Rafael López Aliaga sí cumple con las ollitas comunes",
            "summary": "A través de una conferencia de prensa se detalló el trabajo que se realiza desde la MML.",
            "date": "31 de octubre de 2023",
            "source": "MML",
            "related_candidate_name": "Rafael López Aliaga",
            "full_description": (
                "El alcalde Rafael López Aliaga en compañía de la Gerente de Desarrollo Humano, Isabel Ayala "
                "y las presidentas de distintas ollas comunes de diversos distritos como Rímac, Santa Rosa, Ancón, "
                "San Juan de Miraflores, Villa María del Triunfo, entre otros, explicó la labor que se viene ejecutando "
                "desde la comuna edil para abastecer a las más de 2,000 ollas comunes en Lima Metropolitana."
            ),
            "is_verified": True,
            "image_url": "https://tse2.mm.bing.net/th/id/OIP.x5tI1QlTquTNVm1kdFyKBQHaEK?cb=12&rs=1&pid=ImgDetMain&o=7&rm=3",
            "source_url": "https://www.gob.pe/institucion/munilima/noticias/859856-rafael-lopez-aliaga-si-cumple-con-las-ollitas-comunes"
        },
        {
            "document_id": "doc_actividad_102",
            "title": "Mitin de cierre en Plaza San Martín",
            "summary": "Evento de fin de campaña en el centro de Lima con la participación de candidatos al Congreso.",
            "date": "14 de octubre de 2025",
            "source": "RPP Noticias",
            "related_candidate_name": "Rafael López Aliaga",
            "full_description": (
                "López Aliaga realizó un evento masivo en el centro de Lima, presentando a sus candidatos al congreso. "
                "El mitin estuvo centrado en temas de seguridad ciudadana, prometiendo la compra de nuevas motocicletas "
                "para la policía municipal y la reactivación de proyectos de infraestructura en la capital, destacando "
                "su experiencia en la gestión pública reciente."
            ),
            "is_verified": False,
            "image_url": "https://ojo.pe/resizer/RdDYhL73JIUveYaUOSoXpiWvbLg=/580x330/smart/filters:format(jpeg):quality(75)/cloudfront-us-east-1.images.arcpublishing.com/elcomercio/JHTWBC75RVFABPKXBJMWVGBNTY.jpg",
            "source_url": "https://rpp.pe/actualidad/mitin-rla-san-martin-cierre-campana"
        },

        # Keiko Fujimori (KF)
        {
            "document_id": "doc_noticia_201",
            "title": "Fujimori presenta plan de gobierno enfocado en reactivación económica",
            "summary": "Keiko Fujimori detalla su estrategia post-pandemia en un evento con empresarios y gremios.",
            "date": "18 de octubre de 2025",
            "source": "Perú21",
            "related_candidate_name": "Keiko Fujimori",
            "full_description": (
                "La candidata de Fuerza Popular presentó su plan de gobierno con énfasis en la reactivación económica "
                "post-pandemia, incluyendo medidas de apoyo a las MiPymes y generación de empleo formal. El plan incluye "
                "la creación de un fondo de garantías para microempresas, la reducción de impuestos temporales para los sectores "
                "más afectados y la simplificación de trámites para nuevos negocios."
            ),
            "is_verified": True,
            "image_url": "https://mf.b37mrtl.ru/actualidad/public_images/2021.07/original/60faa33959bf5b65296f2f33.jpg",
            "source_url": "https://peru21.pe/politica/keiko-plan-reactivacion-economica-2026-noticia/"
        },
        {
            "document_id": "doc_documento_203",
            "title": "Fuerza Popular publica versión final de plan de gobierno",
            "summary": "Plan oficial del partido presentado ante el JNE, cumpliendo con los plazos electorales.",
            "date": "21 de septiembre de 2025",
            "source": "JNE",
            "related_candidate_name": "Keiko Fujimori",
            "full_description": (
                "El partido Fuerza Popular publicó la versión consolidada del plan de gobierno ante el Jurado Nacional "
                "de Elecciones (JNE). El documento, de más de 200 páginas, detalla las propuestas en seguridad, economía "
                "y justicia, con un capítulo especial dedicado a la reforma del Estado y la lucha contra la corrupción estructural."
            ),
            "is_verified": True,
            "image_url": "https://imgv2-2-f.scribdassets.com/img/document/388126415/original/405c3d0ee1/1726092831?v=1",
            "source_url": "https://portal.jne.gob.pe/plan-gobierno/fuerza-popular-version-final-2026"
        },

        # César Acuña (CA)
        {
            "document_id": "doc_noticia_301",
            "title": "Acuña promete 'Educación como Revolución'",
            "summary": "Propuesta central del candidato de APP con enfoque en inversión educativa y becas nacionales.",
            "date": "17 de octubre de 2025",
            "source": "La República",
            "related_candidate_name": "César Acuña",
            "full_description": (
                "El candidato de Alianza para el Progreso (APP) centró su discurso en la inversión del 6% del PBI para el sector educativo, "
                "prometiendo la creación de nuevas universidades tecnológicas y un programa masivo de becas 'Beca 18 Plus' para estudiantes "
                "de bajos recursos, buscando reducir la brecha educativa entre la costa y la sierra del país."
            ),
            "is_verified": False,
            "image_url": "https://macronorte.pe/wp-content/uploads/2023/03/WhatsApp-Image-2023-03-07-at-21.24.12.jpg",
            "source_url": "https://larepublica.pe/elecciones/acuna-educacion-revolucion-pbi-noticia/"
        },

        # Martín Vizcarra (MV)
        {
            "document_id": "doc_actividad_501",
            "title": "Vizcarra apela inhabilitación ante TC",
            "summary": "Busca revertir la inhabilitación impuesta por el Congreso para poder participar en las próximas elecciones.",
            "date": "10 de octubre de 2025",
            "source": "Canal N",
            "related_candidate_name": "Martín Vizcarra",
            "full_description": (
                "La defensa legal del expresidente presentó un recurso de agravio constitucional ante el Tribunal Constitucional (TC) "
                "para revertir la inhabilitación por 10 años impuesta por el Congreso. Argumentan una violación al debido proceso y a sus "
                "derechos políticos en la decisión que lo sancionó por el caso 'Vacunagate'. El TC admitió a trámite el recurso y se espera "
                "una decisión en las próximas semanas, lo cual es clave para su candidatura."
            ),
            "is_verified": True,
            "image_url": "https://tse1.mm.bing.net/th/id/OIP.ixCiEaiAAcJlaxUaUBSqUgHaD4?cb=12&w=1200&h=630&rs=1&pid=ImgDetMain&o=7&rm=3",
            "source_url": "https://canaln.pe/actualidad/vizcarra-apela-inhabilitacion-tribunal-constitucional-tc-noticia/"
        },
    ]

        for n in news_data:
            NewsDetail.objects.create(**n)

        # Investigaciones
        investigations  = [
            {
                "document_id": "doc_antecedente_1_1",
                "case_title": "Investigación por Lavado de Activos",
                "case_entity": "Ministerio Público (Fiscalía de la Nación)",
                "case_date": "15/05/2021",
                "status": "Activo - En Indagación Preliminar",
                "timeline": [
                    {"date": "15/05/2021", "title": "Apertura de Investigación Preliminar", "description": "La Fiscalía inicia indagación..."},
                    {"date": "10/08/2022", "title": "Requisitoria Documental", "description": "La fiscalía solicita levantamiento del secreto bancario."},
                    {"date": "01/03/2023", "title": "Declaración del Investigado", "description": "El investigado brinda su testimonio ante el despacho fiscal."}
                ],
                "official_documents": [
                    {"title": "Resolución Fiscal N° 001 - Inicio de Diligencias", "documentUrl": "https://fiscalia.gob.pe/res-rla-001"},
                    {"title": "Requerimiento de Información Bancaria", "documentUrl": "https://fiscalia.gob.pe/req-info-banco"}
                ],
                "involved_parties": [
                    {"name": "Rafael López Aliaga", "role": "Investigado Principal"},
                    {"name": "Empresas del Grupo", "role": "Terceros Involucrados"}
                ]
            },
            {
                "document_id": "doc_antecedente_1_2",
                "case_title": "Proceso Administrativo por Deudas Tributarias",
                "case_entity": "SUNAT",
                "case_date": "01/03/2019",
                "status": "En Proceso de Fraccionamiento y Pago",
                "timeline": [
                    {"date": "01/03/2019", "title": "Emisión de Resolución de Cobranza", "description": "SUNAT emite resolución por deuda pendiente."},
                    {"date": "15/05/2019", "title": "Solicitud de Fraccionamiento", "description": "La defensa presenta solicitud de fraccionamiento."},
                    {"date": "01/07/2019", "title": "Aprobación de Fraccionamiento", "description": "SUNAT aprueba plan de pagos por 36 meses."}
                ],
                "official_documents": [
                    {"title": "Resolución de Deuda SUNAT", "documentUrl": "https://sunat.gob.pe/res-deuda-rla"},
                    {"title": "Acuerdo de Fraccionamiento N° 456-2019", "documentUrl": "https://sunat.gob.pe/acuerdo-rla"}
                ],
                "involved_parties": [
                    {"name": "Empresa X de RLA", "role": "Deudor Principal"}
                ]
            },
            {
                "document_id": "doc_antecedente_2_1",
                "case_title": "Investigación por Aportes de Campaña (Caso Cócteles)",
                "case_entity": "Ministerio Público (Fiscalía de la Nación)",
                "case_date": "20/09/2018",
                "status": "Investigación Formalizada",
                "timeline": [
                    {"date": "20/09/2018", "title": "Inicio de la Investigación", "description": "La Fiscalía inicia indagación por aportes ilícitos."},
                    {"date": "31/10/2018", "title": "Orden de Prisión Preventiva", "description": "Se dicta prisión preventiva, luego revocada por el TC."},
                    {"date": "10/06/2021", "title": "Acusación Formal", "description": "La fiscalía presenta acusación formal ante el Poder Judicial."}
                ],
                "official_documents": [
                    {"title": "Carpeta Fiscal N° 123-2024", "documentUrl": "https://fiscalia.gob.pe/carpeta-123-2024"},
                    {"title": "Resolución del Tribunal Constitucional", "documentUrl": "https://tc.gob.pe/res-fujimori"}
                ],
                "involved_parties": [
                    {"name": "Keiko Fujimori", "role": "Investigada Principal"},
                    {"name": "Vicente Silva Checa", "role": "Co-investigado"},
                    {"name": "Mark Vito Villanella", "role": "Testigo/Co-investigado"}
                ]
            },
            {
                "document_id": "doc_antecedente_3_1",
                "case_title": "Denuncia por Plagio Académico",
                "case_entity": "Comisión de Ética del Congreso / Universidad",
                "case_date": "20/01/2016",
                "status": "Cerrado (Sin Sanción)",
                "timeline": [
                    {"date": "20/01/2016", "title": "Denuncia Pública", "description": "Se revelan presuntos plagios en tesis doctoral."},
                    {"date": "05/02/2016", "title": "Investigación de Comisión de Ética", "description": "El Congreso inicia indagación preliminar."},
                    {"date": "15/03/2016", "title": "Informe de Rectorado", "description": "La universidad declara que no procede la anulación del título."}
                ],
                "official_documents": [
                    {"title": "Informe Final de Comisión de Ética", "documentUrl": "https://congreso.gob.pe/informe-etica-acuña"},
                    {"title": "Comunicado Oficial de Universidad", "documentUrl": "https://universidad.es/comunicado-acuña"}
                ],
                "involved_parties": [
                    {"name": "César Acuña", "role": "Denunciado"},
                    {"name": "Comisión de Ética", "role": "Entidad Investigadora"}
                ]
            },
            {
                "document_id": "doc_antecedente_5_1",
                "case_title": "Inhabilitación Política (Caso Vacunagate)",
                "case_entity": "Congreso de la República",
                "case_date": "16/04/2021",
                "status": "Inhabilitado (10 años)",
                "timeline": [
                    {"date": "01/03/2021", "title": "Revelación Pública", "description": "Se revela vacunación irregular con Sinopharm."},
                    {"date": "16/04/2021", "title": "Decisión Final del Congreso", "description": "El pleno vota a favor de la inhabilitación."},
                    {"date": "10/10/2025", "title": "Apelación ante el TC", "description": "Presenta recurso ante el Tribunal Constitucional."}
                ],
                "official_documents": [
                    {"title": "Resolución Legislativa del Congreso", "documentUrl": "https://congreso.gob.pe/rl-vizcarra"},
                    {"title": "Recurso de Agravio Constitucional", "documentUrl": "https://tc.gob.pe/recurso-vizcarra"}
                ],
                "involved_parties": [
                    {"name": "Martín Vizcarra", "role": "Sancionado/Inhabilitado"},
                    {"name": "Pilar Mazzetti", "role": "Ex-Ministra de Salud"}
                ]
            }
        ]

        for inv in investigations:
            InvestigationDetail.objects.create(**inv)

        self.stdout.write(self.style.SUCCESS("✅ Investigaciones y noticias cargadas correctamente"))
