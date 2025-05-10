from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _
from django.utils.safestring import mark_safe
from django.templatetags.static import static

UNFOLD = {
    "SITE_TITLE": mark_safe(
        """
        <span style="
            font-size: 1.4rem;
            font-weight: 800;
            background: linear-gradient(135deg, #2b6cb0 0%, #68d391 100%);
            -webkit-background-clip: text;
            background-clip: text;
            color: transparent;
        ">Dental29.admin</span>
        <br>
        <span style="
            font-size: 1.1rem;
            color: black;
            font-weight: 400;
        ">Стоматологическая клиника</span>
        """
    ),
    "SITE_HEADER": " ",
    "SITE_ICON": lambda request: static("images/logo/logo_admin.png"),
    "SITE_FAVICONS": [
        {
            "rel": "icon",
            "sizes": "48x48",
            "type": "image/svg+xml",
            "href": lambda request: static("images/logo/favicon.ico"),
        },
    ],
    "SIDEBAR": {
        "show_search": True,
        "show_all_applications": True,
        "navigation": [
            {
                "separator": False,
                "collapsible": False,
                "items": [
                    {
                        "title": _("Информационная панель"),
                        "icon": "monitoring",
                        "link": reverse_lazy("admin:index"),
                    },
                    {
                        "title": _("Журнал записи"),
                        "icon": "auto_stories",
                        "link": reverse_lazy("admin:index"), 
                    },
                ],
            },
            {
                "title": _("Пациенты"),
                "separator": True,
                "collapsible": True,
                "items": [
                    {
                        "title": _("Пациенты"),
                        "icon": "group",
                        "link": reverse_lazy("admin:patients_patient_changelist"),
                    },
                    {
                        "title": _("Типы пациентов"),
                        "icon": "supervisor_account",
                        "link": reverse_lazy("admin:patients_patienttype_changelist"),
                    },
                    {
                        "title": _("Медицинские карты"),
                        "icon": "medical_information",
                        "link": reverse_lazy("admin:patients_medicalcard_changelist"),
                    },
                    {
                        "title": _("Вкладыши мед. карт"),
                        "icon": "description",
                        "link": reverse_lazy("admin:patients_medicalcardinsert_changelist"),
                    },
                    {
                        "title": _("Анкеты здоровья"),
                        "icon": "diagnosis",
                        "link": reverse_lazy("admin:patients_healthquestionnaire_changelist"),
                    },
                    {
                        "title": _("СОПД"),
                        "icon": "inventory",
                        "link": reverse_lazy("admin:patients_personaldataconsent_changelist"),
                    },
                    {
                        "title": _("Непереносимости"),
                        "icon": "vaccines",
                        "link": reverse_lazy("admin:patients_intolerance_changelist"),
                    },
                    {
                        "title": _("Заболевания"),
                        "icon": "coronavirus",
                        "link": reverse_lazy("admin:patients_disease_changelist"),
                    },
                    {
                        "title": _("Контакты"),
                        "icon": "person",
                        "link": reverse_lazy("admin:patients_contactinfo_changelist"),
                    },
                    {
                        "title": _("Типы контактов"),
                        "icon": "person_search",
                        "link": reverse_lazy("admin:patients_contacttype_changelist"),
                    },
                    {
                        "title": _("Пол"),
                        "icon": "wc",
                        "link": reverse_lazy("admin:patients_gender_changelist"),
                    },
                ],
            },
            {
                "title": _("Сотрудники"),
                "separator": True,
                "collapsible": True,
                "items": [
                    {
                        "title": _("Сотрудники"),
                        "icon": "group",
                        "link": reverse_lazy("admin:employees_employee_changelist"),
                    },
                    {
                        "title": _("Должности"),
                        "icon": "work",
                        "link": reverse_lazy("admin:employees_position_changelist"),
                    },
                    {
                        "title": _("Кабинеты"),
                        "icon": "meeting_room",
                        "link": reverse_lazy("admin:employees_cabinet_changelist"),
                    },
                    {
                        "title": _("Статусы"),
                        "icon": "check_circle",
                        "link": reverse_lazy("admin:employees_employeestatus_changelist"),
                    },
                ],
            },
            {
                "title": _("Записи на приём"),
                "separator": True,
                "collapsible": True,
                "items": [
                    {
                        "title": _("Типы приёмов"),
                        "icon": "event_note",
                        "link": reverse_lazy("admin:appointments_appointmenttype_changelist"),
                    },
                    {
                        "title": _("Записи"),
                        "icon": "event",
                        "link": reverse_lazy("admin:appointments_appointment_changelist"),
                    },
                    {
                        "title": _("Отмены записей"),
                        "icon": "event_busy",
                        "link": reverse_lazy("admin:appointments_appointmentcancellation_changelist"),
                    },
                    {
                        "title": _("Расписания"),
                        "icon": "browse_gallery",
                        "link": reverse_lazy("admin:appointments_schedule_changelist"),
                    },
                    {
                        "title": _("Позиции расписания"),
                        "icon": "playlist_add",
                        "link": reverse_lazy("admin:appointments_scheduleposition_changelist"),
                    },
                    {
                        "title": _("Статусы напоминаний"),
                        "icon": "notifications_active",
                        "link": reverse_lazy("admin:appointments_reminderstatus_changelist"),
                    },
                    {
                        "title": _("Дни"),
                        "icon": "calendar_today",
                        "link": reverse_lazy("admin:appointments_day_changelist"),
                    },
                    {
                        "title": _("Статусы дней"),
                        "icon": "event_available",
                        "link": reverse_lazy("admin:appointments_daystatus_changelist"),
                    },
                    {
                        "title": _("Месяцы"),
                        "icon": "calendar_month",
                        "link": reverse_lazy("admin:appointments_month_changelist"),
                    },
                ],
            },
            {
                "title": _("Услуги"),
                "separator": True,
                "collapsible": True,
                "items": [
                    {
                        "title": _("Номенклатура"),
                        "icon": "inventory",
                        "link": reverse_lazy("admin:services_nomenclature_changelist"),
                    },
                    {
                        "title": _("Типы номенклатуры"),
                        "icon": "category",
                        "link": reverse_lazy("admin:services_nomenclaturetype_changelist"),
                    },
                    {
                        "title": _("Единицы измерения"),
                        "icon": "straighten",
                        "link": reverse_lazy("admin:services_unit_changelist"),
                    },
                    {
                        "title": _("Прайс-листы"),
                        "icon": "attach_money",
                        "link": reverse_lazy("admin:services_pricelist_changelist"),
                    },
                    {
                        "title": _("Позиции прайс-листа"),
                        "icon": "list",
                        "link": reverse_lazy("admin:services_pricelistitem_changelist"),
                    },
                    {
                        "title": _("Услуги на приёме"),
                        "icon": "medical_services",
                        "link": reverse_lazy("admin:services_serviceonappointment_changelist"),
                    },
                    {
                        "title": _("Манипуляции"),
                        "icon": "build",
                        "link": reverse_lazy("admin:services_manipulation_changelist"),
                    },
                ],
            },
            {
                "title": _("Договоры"),
                "separator": True,
                "collapsible": True,
                "items": [
                    {
                        "title": _("Договоры"),
                        "icon": "description",
                        "link": reverse_lazy("admin:contracts_contract_changelist"),
                    },
                    {
                        "title": _("Приложения к договорам"),
                        "icon": "attachment",
                        "link": reverse_lazy("admin:contracts_contractappendix_changelist"),
                    },
                    {
                        "title": _("Оплаты"),
                        "icon": "payment",
                        "link": reverse_lazy("admin:contracts_payment_changelist"),
                    },
                    {
                        "title": _("Документы"),
                        "icon": "article",
                        "link": reverse_lazy("admin:contracts_document_changelist"),
                    },
                    {
                        "title": _("Типы документов"),
                        "icon": "folder",
                        "link": reverse_lazy("admin:contracts_documenttype_changelist"),
                    },
                    {
                        "title": _("Статусы документов"),
                        "icon": "check_circle",
                        "link": reverse_lazy("admin:contracts_documentstatus_changelist"),
                    },
                    {
                        "title": _("ИДС"),
                        "icon": "approval",
                        "link": reverse_lazy("admin:contracts_informedconsent_changelist"),
                    },
                ],
            },
            {
                "title": _("Зубная Система"),
                "separator": True,
                "collapsible": True,
                "items": [
                    {
                        "title": _("Диагнозы"),
                        "icon": "diagnosis",
                        "link": reverse_lazy("admin:dental_diagnosis_changelist"),
                    },
                    {
                        "title": _("Зубные формулы"),
                        "icon": "dentistry",
                        "link": reverse_lazy("admin:dental_toothformula_changelist"),
                    },
                    {
                        "title": _("Зубы"),
                        "icon": "dentistry",
                        "link": reverse_lazy("admin:dental_tooth_changelist"),
                    },
                    {
                        "title": _("Позиции зубов"),
                        "icon": "format_list_numbered",
                        "link": reverse_lazy("admin:dental_toothposition_changelist"),
                    },
                    {
                        "title": _("Статусы зубов"),
                        "icon": "checklist",
                        "link": reverse_lazy("admin:dental_toothstatus_changelist"),
                    },
                    {
                        "title": _("Назначения"),
                        "icon": "prescriptions",
                        "link": reverse_lazy("admin:dental_prescription_changelist"),
                    },
                ],
            },
            {
                "title": _("Адреса"),
                "separator": True,
                "collapsible": True,
                "items": [
                    {
                        "title": _("Адреса"),
                        "icon": "location_on",
                        "link": reverse_lazy("admin:addresses_address_changelist"),
                    },
                    {
                        "title": _("Улицы"),
                        "icon": "signpost",
                        "link": reverse_lazy("admin:addresses_street_changelist"),
                    },
                    {
                        "title": _("Населённые пункты"),
                        "icon": "location_city",
                        "link": reverse_lazy("admin:addresses_settlement_changelist"),
                    },
                    {
                        "title": _("Типы населённых пунктов"),
                        "icon": "apartment",
                        "link": reverse_lazy("admin:addresses_settlementtype_changelist"),
                    },
                    {
                        "title": _("Регионы"),
                        "icon": "map",
                        "link": reverse_lazy("admin:addresses_region_changelist"),
                    },
                    {
                        "title": _("Страны"),
                        "icon": "public",
                        "link": reverse_lazy("admin:addresses_country_changelist"),
                    },
                ],
            },
        ],
    },
    "COLORS": {
        "primary": {
            "50": "240 249 255",
            "100": "220 238 255",
            "200": "191 227 255",
            "300": "147 205 255",
            "400": "96 175 255",
            "500": "59 141 255",
            "600": "37 112 235",
            "700": "29 90 216",
            "800": "30 75 175",
            "900": "30 65 138",
        }
    },
    "TABS": [
        {
            "models": ["patients.patient"],
            "items": [
                {
                    "title": _("Профиль пациента"),
                    "link": lambda context: (
                        reverse_lazy("admin:patients_patient_change", args=[context["object_id"]])
                        if isinstance(context, dict) and "object_id" in context
                        else reverse_lazy("admin:patients_patient_changelist")
                    ),
                },
                {
                    "title": _("Медицинская карта"),
                    "link": lambda context: (
                        f"{reverse_lazy('admin:patients_medicalcard_changelist')}?patient__id__exact={context['object_id']}"
                        if isinstance(context, dict) and "object_id" in context
                        else reverse_lazy("admin:patients_medicalcard_changelist")
                    ),
                },
                {
                    "title": _("Записи на приём"),
                    "link": lambda context: (
                        f"{reverse_lazy('admin:appointments_appointment_changelist')}?patient__id__exact={context['object_id']}"
                        if isinstance(context, dict) and "object_id" in context
                        else reverse_lazy("admin:appointments_appointment_changelist")
                    ),
                },
                {
                    "title": _("Договоры"),
                    "link": lambda context: (
                        f"{reverse_lazy('admin:contracts_contract_changelist')}?patient__id__exact={context['object_id']}"
                        if isinstance(context, dict) and "object_id" in context
                        else reverse_lazy("admin:contracts_contract_changelist")
                    ),
                },
                {
                    "title": _("ИДС"),
                    "link": lambda context: (
                        f"{reverse_lazy('admin:contracts_informedconsent_changelist')}?patient__id__exact={context['object_id']}"
                        if isinstance(context, dict) and "object_id" in context
                        else reverse_lazy("admin:contracts_informedconsent_changelist")
                    ),
                },
                {
                    "title": _("Согласия на данные"),
                    "link": lambda context: (
                        f"{reverse_lazy('admin:patients_personaldataconsent_changelist')}?patient__id__exact={context['object_id']}"
                        if isinstance(context, dict) and "object_id" in context
                        else reverse_lazy("admin:patients_personaldataconsent_changelist")
                    ),
                },
                {
                    "title": _("Анкеты здоровья"),
                    "link": lambda context: (
                        f"{reverse_lazy('admin:patients_healthquestionnaire_changelist')}?patient__id__exact={context['object_id']}"
                        if isinstance(context, dict) and "object_id" in context
                        else reverse_lazy("admin:patients_healthquestionnaire_changelist")
                    ),
                },
                {
                    "title": _("Контакты"),
                    "link": lambda context: (
                        f"{reverse_lazy('admin:patients_contactinfo_changelist')}?patient__id__exact={context['object_id']}"
                        if isinstance(context, dict) and "object_id" in context
                        else reverse_lazy("admin:patients_contactinfo_changelist")
                    ),
                },
                {
                    "title": _("Зубные формулы"),
                    "link": lambda context: (
                        f"{reverse_lazy('admin:dental_toothformula_changelist')}?medical_card__patient__id__exact={context['object_id']}"
                        if isinstance(context, dict) and "object_id" in context
                        else reverse_lazy("admin:dental_toothformula_changelist")
                    ),
                },
                {
                    "title": _("Непереносимости"),
                    "link": lambda context: (
                        f"{reverse_lazy('admin:patients_intolerance_changelist')}?medical_card__patient__id__exact={context['object_id']}"
                        if isinstance(context, dict) and "object_id" in context
                        else reverse_lazy("admin:patients_intolerance_changelist")
                    ),
                },
                {
                    "title": _("Заболевания"),
                    "link": lambda context: (
                        f"{reverse_lazy('admin:patients_disease_changelist')}?medical_card__patient__id__exact={context['object_id']}"
                        if isinstance(context, dict) and "object_id" in context
                        else reverse_lazy("admin:patients_disease_changelist")
                    ),
                },
            ],
        },
        {
            "models": ["employees.employee"],
            "items": [
                {
                    "title": _("Профиль сотрудника"),
                    "link": lambda context: (
                        reverse_lazy("admin:employees_employee_change", args=[context["object_id"]])
                        if isinstance(context, dict) and "object_id" in context
                        else reverse_lazy("admin:employees_employee_changelist")
                    ),
                },
                {
                    "title": _("Записи на приём"),
                    "link": lambda context: (
                        f"{reverse_lazy('admin:appointments_appointment_changelist')}?employee__id__exact={context['object_id']}"
                        if isinstance(context, dict) and "object_id" in context
                        else reverse_lazy("admin:appointments_appointment_changelist")
                    ),
                },
                {
                    "title": _("Позиции расписания"),
                    "link": lambda context: (
                        f"{reverse_lazy('admin:appointments_scheduleposition_changelist')}?employee__id__exact={context['object_id']}"
                        if isinstance(context, dict) and "object_id" in context
                        else reverse_lazy("admin:appointments_scheduleposition_changelist")
                    ),
                },
                {
                    "title": _("Договоры"),
                    "link": lambda context: (
                        f"{reverse_lazy('admin:contracts_contract_changelist')}?employee__id__exact={context['object_id']}"
                        if isinstance(context, dict) and "object_id" in context
                        else reverse_lazy("admin:contracts_contract_changelist")
                    ),
                },
                {
                    "title": _("ИДС"),
                    "link": lambda context: (
                        f"{reverse_lazy('admin:contracts_informedconsent_changelist')}?employee__id__exact={context['object_id']}"
                        if isinstance(context, dict) and "object_id" in context
                        else reverse_lazy("admin:contracts_informedconsent_changelist")
                    ),
                },
                {
                    "title": _("Прайс-листы"),
                    "link": lambda context: (
                        f"{reverse_lazy('admin:services_pricelist_changelist')}?employee__id__exact={context['object_id']}"
                        if isinstance(context, dict) and "object_id" in context
                        else reverse_lazy("admin:services_pricelist_changelist")
                    ),
                },
                {
                    "title": _("Контакты"),
                    "link": lambda context: (
                        f"{reverse_lazy('admin:patients_contactinfo_changelist')}?employee__id__exact={context['object_id']}"
                        if isinstance(context, dict) and "object_id" in context
                        else reverse_lazy("admin:patients_contactinfo_changelist")
                    ),
                },
            ],
        },
        {
            "models": ["patients.medicalcard"],
            "items": [
                {
                    "title": _("Медицинская карта"),
                    "link": lambda context: (
                        reverse_lazy("admin:patients_medicalcard_change", args=[context["object_id"]])
                        if isinstance(context, dict) and "object_id" in context
                        else reverse_lazy("admin:patients_medicalcard_changelist")
                    ),
                },
                {
                    "title": _("Вкладыши"),
                    "link": lambda context: (
                        f"{reverse_lazy('admin:patients_medicalcardinsert_changelist')}?medical_card__id__exact={context['object_id']}"
                        if isinstance(context, dict) and "object_id" in context
                        else reverse_lazy("admin:patients_medicalcardinsert_changelist")
                    ),
                },
                {
                    "title": _("Зубные формулы"),
                    "link": lambda context: (
                        f"{reverse_lazy('admin:dental_toothformula_changelist')}?medical_card__id__exact={context['object_id']}"
                        if isinstance(context, dict) and "object_id" in context
                        else reverse_lazy("admin:dental_toothformula_changelist")
                    ),
                },
                {
                    "title": _("Непереносимости"),
                    "link": lambda context: (
                        f"{reverse_lazy('admin:patients_intolerance_changelist')}?medical_card__id__exact={context['object_id']}"
                        if isinstance(context, dict) and "object_id" in context
                        else reverse_lazy("admin:patients_intolerance_changelist")
                    ),
                },
                {
                    "title": _("Заболевания"),
                    "link": lambda context: (
                        f"{reverse_lazy('admin:patients_disease_changelist')}?medical_card__id__exact={context['object_id']}"
                        if isinstance(context, dict) and "object_id" in context
                        else reverse_lazy("admin:patients_disease_changelist")
                    ),
                },
                {
                    "title": _("Назначения"),
                    "link": lambda context: (
                        f"{reverse_lazy('admin:dental_prescription_changelist')}?medical_card__id__exact={context['object_id']}"
                        if isinstance(context, dict) and "object_id" in context
                        else reverse_lazy("admin:dental_prescription_changelist")
                    ),
                },
                {
                    "title": _("Пациент"),
                    "link": lambda context: (
                        reverse_lazy("admin:patients_patient_change", args=[context["original"].patient.id])
                        if isinstance(context, dict) and "original" in context and hasattr(context["original"], "patient")
                        else reverse_lazy("admin:patients_patient_changelist")
                    ),
                },
            ],
        },
        {
            "models": ["appointments.appointment"],
            "items": [
                {
                    "title": _("Запись на приём"),
                    "link": lambda context: (
                        reverse_lazy("admin:appointments_appointment_change", args=[context["object_id"]])
                        if isinstance(context, dict) and "object_id" in context
                        else reverse_lazy("admin:appointments_appointment_changelist")
                    ),
                },
                {
                    "title": _("Услуги на приёме"),
                    "link": lambda context: (
                        f"{reverse_lazy('admin:services_serviceonappointment_changelist')}?appointment__id__exact={context['object_id']}"
                        if isinstance(context, dict) and "object_id" in context
                        else reverse_lazy("admin:services_serviceonappointment_changelist")
                    ),
                },
                {
                    "title": _("Отмена записи"),
                    "link": lambda context: (
                        f"{reverse_lazy('admin:appointments_appointmentcancellation_changelist')}?appointment__id__exact={context['object_id']}"
                        if isinstance(context, dict) and "object_id" in context
                        else reverse_lazy("admin:appointments_appointmentcancellation_changelist")
                    ),
                },
                {
                    "title": _("Пациент"),
                    "link": lambda context: (
                        reverse_lazy("admin:patients_patient_change", args=[context["original"].patient.id])
                        if isinstance(context, dict) and "original" in context and hasattr(context["original"], "patient")
                        else reverse_lazy("admin:patients_patient_changelist")
                    ),
                },
                {
                    "title": _("Сотрудник"),
                    "link": lambda context: (
                        reverse_lazy("admin:employees_employee_change", args=[context["original"].employee.id])
                        if isinstance(context, dict) and "original" in context and hasattr(context["original"], "employee")
                        else reverse_lazy("admin:employees_employee_changelist")
                    ),
                },
            ],
        },
        {
            "models": ["contracts.contract"],
            "items": [
                {
                    "title": _("Договор"),
                    "link": lambda context: (
                        reverse_lazy("admin:contracts_contract_change", args=[context["object_id"]])
                        if isinstance(context, dict) and "object_id" in context
                        else reverse_lazy("admin:contracts_contract_changelist")
                    ),
                },
                {
                    "title": _("Приложения"),
                    "link": lambda context: (
                        f"{reverse_lazy('admin:contracts_contractappendix_changelist')}?contract__id__exact={context['object_id']}"
                        if isinstance(context, dict) and "object_id" in context
                        else reverse_lazy("admin:contracts_contractappendix_changelist")
                    ),
                },
                {
                    "title": _("Оплаты"),
                    "link": lambda context: (
                        f"{reverse_lazy('admin:contracts_payment_changelist')}?contract__id__exact={context['object_id']}"
                        if isinstance(context, dict) and "object_id" in context
                        else reverse_lazy("admin:contracts_payment_changelist")
                    ),
                },
                {
                    "title": _("Пациент"),
                    "link": lambda context: (
                        reverse_lazy("admin:patients_patient_change", args=[context["original"].patient.id])
                        if isinstance(context, dict) and "original" in context and hasattr(context["original"], "patient")
                        else reverse_lazy("admin:patients_patient_changelist")
                    ),
                },
                {
                    "title": _("Сотрудник"),
                    "link": lambda context: (
                        reverse_lazy("admin:employees_employee_change", args=[context["original"].employee.id])
                        if isinstance(context, dict) and "original" in context and hasattr(context["original"], "employee")
                        else reverse_lazy("admin:employees_employee_changelist")
                    ),
                },
            ],
        },
    ],
}