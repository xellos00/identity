DEFAULT_PROVIDERS = [{
    'provider': 'aws',
    'name': 'AWS',
    'template': {
        'service_account': {
            'schema': {
                'type': 'object',
                'properties': {
                    'account_id': {
                        'title': 'Account ID',
                        'type': 'string',
                        'minLength': 4
                    }
                },
                'required': ['account_id']
            }
        }
    },
    'metadata': {
        'view': {
            'layouts': {
                'help:service_account:create': {
                    'name': 'Creation Help',
                    'type': 'markdown',
                    'options': {
                        'markdown': {
                            'en': (
                                '# Help for AWS Users\n'
                                '&nbsp;\n'
                                '## Find Your AWS Account ID\n'
                                'Get your AWS Account ID.\n'
                                '- [AWS Account ID](https://docs.aws.amazon.com/IAM/latest/UserGuide/console_account-alias.html)\n\n'
                                '&nbsp;\n'
                                '## Get Your Assume role\n'
                                'Granting permissions to create temporary security credentials.\n'
                                '- [AWS Assume Role](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_permissions-to-switch.html)\n\n'
                                '&nbsp;\n'
                                '## Issue AWS Access Key \n'
                                'Get your AWS Access Key & AWS Secret Key\n'
                                '- [AWS Access Key & AWS Secret Key](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_access-keys.html#Using_CreateAccessKey)\n\n'
                            ),
                            'ko': (
                                '# AWS 이용자 가이드\n'
                                '&nbsp;\n'
                                '## AWS 어카운트 아이디(Account ID) 찾기\n'
                                '사용자의 AWS 어카운트 아이디 AWS 콘솔(Console)에서 확인하기\n'
                                '- [AWS Account ID](https://docs.aws.amazon.com/ko_kr/IAM/latest/UserGuide/console_account-alias.html)\n\n'
                                '&nbsp;\n'
                                '## Assume role 획득하기\n'
                                '임시 보안 자격증명을 만들 수있는 권한을 부여하기.\n'
                                '- [AWS Assume Role](https://docs.aws.amazon.com/ko_kr/IAM/latest/UserGuide/id_roles_use_permissions-to-switch.html)\n\n'
                                '&nbsp;\n'
                                '## AWS Access Key 발급하기\n'
                                'AWS Access Key & AWS Secret Key 발급하기\n'
                                '- [AWS Access Key & AWS Secret Key](https://docs.aws.amazon.com/ko_kr/IAM/latest/UserGuide/id_credentials_access-keys.html#Using_CreateAccessKey)\n\n'
                            ),

                        }
                    }
                }
            }
        }
    },
    'capability': {
        'supported_schema': ['aws_access_key', 'aws_assume_role']
    },
    'tags': {
        'color': '#FF9900',
        'icon': 'https://assets-console-spaceone-stg.s3.ap-northeast-2.amazonaws.com/console-assets/icons/aws.svg',
        'external_link_template': 'https://<%- data.account_id %>.signin.aws.amazon.com/console'
    }
}, {
    'provider': 'google_cloud',
    'version': 'v1',
    'name': 'Google Cloud',
    'template': {
        'service_account': {
            'schema': {
                'type': 'object',
                'properties': {
                    'project_id': {
                        'title': 'Project ID',
                        'type': 'string',
                        'minLength': 4
                    }
                },
                'required': ['project_id']
            }
        }
    },
    'metadata': {
        'view': {
            'layouts': {
                'help:service_account:create': {
                    'name': 'Creation Help',
                    'type': 'markdown',
                    'options': {
                        'markdown': {
                            'en': (
                                '# Getting started with Google Cloud\n'
                                '&nbsp;\n'
                                '## Identifying Your Project\n'
                                'Get your Project infos (Project Name, Project ID and Project number)\n'
                                '- [Project Info](https://cloud.google.com/resource-manager/docs/creating-managing-projects#identifying_projects)\n\n'
                                '&nbsp;\n'
                                '## Get Your Service Account Key(JSON)\n'
                                'Generate Your a JSON Service Account Key.\n'
                                '- [Service Account Key](https://cloud.google.com/docs/authentication/getting-started)\n\n'
                            ),
                            'ko': (
                                '# Google Cloud 시작 가이드\n'
                                '&nbsp;\n'
                                '## Project 정보 확인하기\n'
                                '프로젝트 명, 프로젝트 아이디 프로젝트 번호등등의 프로젝트 정보 확인하기\n'
                                '- [Project Info](https://cloud.google.com/resource-manager/docs/creating-managing-projects?hl=ko#identifying_projects)\n\n'
                                '&nbsp;\n'
                                '## 서비스 어카운트 키(JSON) 받기\n'
                                'JSON 포멧의 서비스 어카운트 키를 생성하기.\n'
                                '- [Service Account Key](https://cloud.google.com/docs/authentication/getting-started?hl=ko)\n\n'
                            ),

                        }
                    }
                }
            }
        }
    },
    'capability': {
        'supported_schema': ['google_oauth_client_id']
    },
    'tags': {
        'color': '#4285F4',
        'icon': 'https://assets-console-spaceone-stg.s3.ap-northeast-2.amazonaws.com/console-assets/icons/google_cloud.svg',
        'external_link_template': 'https://console.cloud.google.com/home/dashboard?project=<%- data.project_id %>'
    }
}, {
    'provider': 'azure',
    'name': 'Microsoft Azure',
    'template': {
        'service_account': {
            'schema': {
                'type': 'object',
                'properties': {
                    'tenant_id': {
                        'title': 'Tenant ID',
                        'type': 'string',
                        'minLength': 4
                    },
                    'subscription_id': {
                        'title': 'Subscription ID',
                        'type': 'string',
                        'minLength': 4
                    }
                },
                'required': ['tenant_id', 'subscription_id']
            }
        }
    },
    'capability': {
        'supported_schema': ['azure_client_secret']
    },
    'tags': {
        'color': '#00BCF2',
        'icon': 'https://assets-console-spaceone-stg.s3.ap-northeast-2.amazonaws.com/console-assets/icons/azure.svg'
    }
}, {
    'provider': 'megazone',
    'name': 'MEGAZONE',
    'template': {
        'service_account': {
            'schema': {}
        }
    },
    'capability': {
        'supported_schema': []
    },
    'tags': {
        'color': '#000000',
        'icon': 'https://assets-console-spaceone-stg.s3.ap-northeast-2.amazonaws.com/console-assets/icons/megazone.svg'
    }
}]

aws_access_key = {
    'name': 'aws_access_key',
    'service_type': 'secret.credentials',
    'schema': {
        'required': [
            'aws_access_key_id',
            'aws_secret_access_key'
        ],
        'properties': {
            'aws_access_key_id': {
                'title': 'AWS Access Key',
                'type': 'string',
                'minLength': 4
            },
            'region_name': {
                'title': 'Region',
                'type': 'string',
                'minLength': 4,
                'examples': [
                    'ap-northeast-2'
                ]
            },
            'aws_secret_access_key': {
                'type': 'string',
                'minLength': 4,
                'title': 'AWS Secret Key'
            }
        },
        'type': 'object'
    },
    'labels': ['AWS'],
    'tags': {
        'description': 'AWS Access Key'
    }
}

aws_assume_role = {
    'name': 'aws_assume_role',
    'service_type': 'secret.credentials',
    'schema': {
        'required': [
            'aws_access_key_id',
            'aws_secret_access_key',
            'role_arn'
        ],
        'properties': {
            'role_arn': {
                'title': 'Role ARN',
                'type': 'string',
                'minLength': 4
            },
            'aws_access_key_id': {
                'title': 'AWS Access Key',
                'type': 'string',
                'minLength': 4
            },
            'region_name': {
                'title': 'Region',
                'type': 'string',
                'minLength': 4,
                'examples': [
                    'ap-northeast-2'
                ]
            },
            'aws_secret_access_key': {
                'type': 'string',
                'minLength': 4,
                'title': 'AWS Secret Key'
            }
        },
        'type': 'object'
    },
    'labels': ['AWS', 'Assume Role'],
    'tags': {
        'description': 'AWS Assume Role'
    }
}

google_api_key = {
    'name': 'google_api_key',
    'service_type': 'secret.credentials',
    'schema': {
        'required': [
            'api_key'
        ],
        'properties': {
            'api_key': {
                'title': 'API Key',
                'type': 'string',
                'minLength': 4
            }
        },
        'type': 'object'
    },
    'labels': ['Google Cloud', 'GCP'],
    'tags': {
        'description': 'Google API Key'
    }
}

google_oauth_client_id = {
    'name': 'google_oauth_client_id',
    'service_type': 'secret.credentials',
    'schema': {
        'properties': {
            'auth_provider_x509_cert_url': {
                'title': 'Auth Provider Cert URL',
                'type': 'string',
                'minLength': 4,
                'default': 'https://www.googleapis.com/oauth2/v1/certs'
            },
            'client_id': {
                'title': 'Client ID',
                'type': 'string',
                'minLength': 4,
                'examples': [
                    '10118252.....'
                ]
            },
            'token_uri': {
                'type': 'string',
                'minLength': 4,
                'default': 'https://oauth2.googleapis.com/token',
                'title': 'Token URI'
            },
            'zone': {
                'type': 'string',
                'minLength': 4,
                'examples': [
                    'asia-northeast3'
                ],
                'title': 'Region'
            },
            'client_x509_cert_url': {
                'type': 'string',
                'minLength': 4,
                'examples': [
                    'https://www.googleapis.com/...'
                ],
                'title': 'client_x509_cert_url'
            },
            'project_id': {
                'type': 'string',
                'minLength': 4,
                'examples': [
                    'project-id'
                ],
                'title': 'Project ID'
            },
            'private_key_id': {
                'type': 'string',
                'minLength': 4,
                'examples': [
                    '771823abcd...'
                ],
                'title': 'Private Key ID'
            },
            'auth_uri': {
                'type': 'string',
                'minLength': 4,
                'default': 'https://acounts.google.com/o/oauth2/auth',
                'title': 'Auth URI'
            },
            'type': {
                'default': 'service_account',
                'title': 'Type',
                'type': 'string',
                'minLength': 4
            },
            'client_email': {
                'type': 'string',
                'minLength': 4,
                'exmaples': [
                    '<api-name>api@project-id.iam.gserviceaccount.com'
                ],
                'title': 'Client Email'
            },
            'private_key': {
                'type': 'string',
                'minLength': 4,
                'examples': [
                    '-----BEGIN'
                ],
                'title': 'Private Key'
            }
        },
        'type': 'object',
        'required': [
            'type',
            'project_id',
            'private_key_id',
            'private_key',
            'client_email',
            'client_id',
            'auth_uri',
            'token_uri',
            'auth_provider_x509_cert_url',
            'client_x509_cert_url'
        ]
    },
    'labels': ['Google Cloud', 'GCP', 'OAuth2.0'],
    'tags': {
        'description': 'Google OAuth Client ID'
    }
}

azure_client_secret = {
    'name': 'azure_client_secret',
    'service_type': 'secret.credentials',
    'schema': {
        'required': [
            'client_id',
            'client_secret',
            'tenant_id',
            'subscription_id'
        ],
        'properties': {
            'client_id': {
                'title': 'Client ID',
                'type': 'string',
                'minLength': 4
            },
            'client_secret': {
                'title': 'Client Secret',
                'type': 'string',
                'minLength': 4
            },
            'tenant_id': {
                'title': 'Tenant ID',
                'type': 'string',
                'minLength': 4
            },
            'subscription_id': {
                'title': 'Subscription ID',
                'type': 'string',
                'minLength': 4
            }
        },
        'type': 'object'
    },
    'labels': ['Azure'],
    'tags': {
        'description': 'Azure Client Secret'
    }
}
