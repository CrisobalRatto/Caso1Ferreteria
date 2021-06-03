$(document).ready(function () {
    $('#contact_form').bootstrapValidator({
        // To use feedback icons, ensure that you use Bootstrap v3.1.0 or later
        feedbackIcons: {
            valid: 'glyphicon glyphicon-ok',
            invalid: 'glyphicon glyphicon-remove',
            validating: 'glyphicon glyphicon-refresh'
        },
        fields: {
            first_name: {
                validators: {
                    stringLength: {
                        min: 2,
                    },
                    notEmpty: {
                        message: 'Ingrese su primer nombre'
                    }
                }
            },
            last_name: {
                validators: {
                    stringLength: {
                        min: 2,
                    },
                    notEmpty: {
                        message: 'Ingrese Apellido'
                    }
                }
            },
           
            user_password: {
                validators: {
                    stringLength: {
                        min: 8,
                    },
                    notEmpty: {
                        message: 'Ingrese contrasena'
                    }
                }
            },
            confirm_password: {
                validators: {
                    stringLength: {
                        min: 8,
                    },
                    notEmpty: {
                        message: 'Confirme su contrasena'
                    }
                }
            },
            email: {
                validators: {
                    notEmpty: {
                        message: 'Ingrese su emil'
                    },
                    emailAddress: {
                        message: 'Ingrese un email valido'
                    }
                }
            },
           
                department: {
                    validators: {
                        notEmpty: {
                            message: 'Seleccione'
                        }
                    }
                },
            }
        }
    })
        .on('success.form.bv', function (e) {
            $('#success_message').slideDown({ opacity: "show" }, "slow") // Do something ...
            $('#contact_form').data('bootstrapValidator').resetForm();

            // Prevent form submission
            e.preventDefault();

            // Get the form instance
            var $form = $(e.target);

            // Get the BootstrapValidator instance
            var bv = $form.data('bootstrapValidator');

            // Use Ajax to submit form data
            $.post($form.attr('action'), $form.serialize(), function (result) {
                console.log(result);
            }, 'json');
        });
});