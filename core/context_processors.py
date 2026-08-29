from account.models import User, Curator, Group

def user_information(request):
	if request.user.is_authenticated:
		context = {
			"user_types": dict(User.USER_ROLES)
		}

		if request.user.role == "C":
			try:
				curator = Curator.objects.get(user=request.user)
				group = Group.objects.get(curator=curator)
				context["group_uuid"] = group.uuid
			except:
				context["nogroup"] = True
				return context

		return context
	
	return {}