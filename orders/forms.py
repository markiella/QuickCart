from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Row, Column, Div
from .models import Order

class CheckoutForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['customer_name', 'customer_email', 'customer_phone', 'delivery_address', 'payment_method', 'notes']
        widgets = {
            'delivery_address': forms.Textarea(attrs={'rows': 3}),
            'notes': forms.Textarea(attrs={'rows': 2, 'placeholder': 'Special instructions (optional)'}),
        }
    
    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)
        
        # Pre-fill form with user data if available
        if user and user.is_authenticated:
            self.fields['customer_name'].initial = f"{user.first_name} {user.last_name}".strip()
            self.fields['customer_email'].initial = user.email
            self.fields['customer_phone'].initial = user.phone_number
            self.fields['delivery_address'].initial = user.address
        
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Row(
                Column('customer_name', css_class='form-group col-md-6 mb-0'),
                Column('customer_email', css_class='form-group col-md-6 mb-0'),
                css_class='form-row'
            ),
            Row(
                Column('customer_phone', css_class='form-group col-md-6 mb-0'),
                Column('payment_method', css_class='form-group col-md-6 mb-0'),
                css_class='form-row'
            ),
            'delivery_address',
            'notes',
            Div(
                Submit('submit', 'Place Order', css_class='btn btn-primary btn-lg w-100'),
                css_class='mt-3'
            )
        )

class OrderStatusForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['status', 'assigned_staff']
    
    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)
        # Filter staff users only
        from django.contrib.auth import get_user_model
        User = get_user_model()
        self.fields['assigned_staff'].queryset = User.objects.filter(role='staff', is_active=True)
        
        # For riders, hide the assigned_staff field (they can only update status)
        if user and user.role == 'rider':
            self.fields.pop('assigned_staff', None)
            self.helper = FormHelper()
            self.helper.layout = Layout(
                'status',
                Submit('submit', 'Update Delivery Status', css_class='btn btn-primary')
            )
        else:
            self.helper = FormHelper()
            self.helper.layout = Layout(
                'status',
                'assigned_staff',
                Submit('submit', 'Update Order', css_class='btn btn-primary')
            )
